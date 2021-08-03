class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        a = []
        n = len(arr)
        for i in range(n):
            if i == 0:
                a.append(arr[i])
            else:
                a.append(arr[i] ^ a[-1])

        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j, n):
                    x = a[j - 1] ^ (0 if i == 0 else a[i - 1])
                    y = a[k] ^ a[j - 1]
                    if x == y:
                        ans += 1
        return ans
