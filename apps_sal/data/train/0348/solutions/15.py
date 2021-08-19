class Solution:

    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        s = sum(arr)
        pref = [0]
        for arr_i in arr:
            pref.append(pref[-1] + arr_i)
        for i in range(1, n + 1):
            pref[i] = min(pref[i], pref[i - 1])
        suf = [0]
        for arr_i in arr[::-1]:
            suf.append(suf[-1] + arr_i)
        for i in range(1, n + 1):
            suf[i] = min(suf[i], suf[i - 1])
        ans = s
        for i in range(n):
            if arr[i] < 0:
                if i - 1 >= 0:
                    ans = max(ans, s - arr[i] - pref[i - 1] - suf[n - 1 - i])
                if n - 2 - i >= 0:
                    ans = max(ans, s - arr[i] - pref[i] - suf[n - 2 - i])
        return ans
