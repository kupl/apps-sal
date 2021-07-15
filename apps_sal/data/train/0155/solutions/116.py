class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        a = []
        jump = [0]*len(arr)
        result = 0
        for i in range(len(arr)):
            a.append((i,arr[i]))
        a.sort(key = lambda x:x[1])
        for i in range(len(arr)):
            l = a[i][0] - 1
            r = a[i][0] + 1
            m = 0
            while (l >= 0 and arr[l] < a[i][1] and a[i][0] - l <= d):
                m = max(m,jump[l])
                l -= 1
            while (r < len(arr) and arr[r] < a[i][1] and r - a[i][0] <= d):
                m = max(m, jump[r])
                r += 1
            jump[a[i][0]] = m + 1
            result = max(result, m + 1)
        return result

