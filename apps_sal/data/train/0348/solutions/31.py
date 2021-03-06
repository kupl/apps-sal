class Solution:

    def maximumSum(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        ans = arr[0]
        n = len(arr)
        s = []
        for i in range(n):
            s.append([None, None])
        s[0][0] = s[0][1] = arr[0]
        for i in range(1, n):
            s[i][0] = max(s[i - 1][0], 0) + arr[i]
            s[i][1] = max(max(s[i - 1][1], 0) + arr[i], s[i - 1][0])
            ans = max(s[i][0], s[i][1], ans)
        print(s)
        return ans
