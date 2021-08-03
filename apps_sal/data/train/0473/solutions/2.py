class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for i in range(n):
            p1 = [0] * (n + 1)
            p1[i] = arr[i]
            for j in range(i + 1, n):
                p1[j] = p1[j - 1] ^ arr[j]
                p2 = [0] * (n + 1)
                for k in range(j, n):
                    p2[k] = p2[k - 1] ^ arr[k]
                    if p1[j - 1] == p2[k]:
                        ans += 1
        return ans
