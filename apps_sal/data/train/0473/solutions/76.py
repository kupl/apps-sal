class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        store = [0]
        n = len(arr)
        for i in range(n):
            store.append(arr[i] ^ store[i])
        ans = 0
        for i in range(1, n):
            for k in range(i + 1, n + 1):
                if store[i - 1] == store[k]:
                    ans += k - i
        return ans
