class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        ans = -1
        start_set = {}
        end_set = {}
        counter = 0
        for idx, n in enumerate(arr):
            if n - 1 in end_set and n + 1 in start_set:
                st = end_set.pop(n-1)
                ed = start_set.pop(n+1)
                end_set[ed] = st
                start_set[st] = ed
                if n - st == m:
                    counter -= 1
                if ed - n == m:
                    counter -= 1
                if ed - st + 1 == m:
                    counter += 1
            elif n - 1 in end_set:
                st = end_set.pop(n-1)
                end_set[n] = st
                start_set[st] = n
                if n - st == m:
                    counter -= 1
                elif n-st+1 == m:
                    counter += 1
            elif n + 1 in start_set:
                ed = start_set.pop(n+1)
                start_set[n] = ed
                end_set[ed] = n
                if ed - n == m:
                    counter -= 1
                elif ed-n+1 == m:
                    counter += 1
            else:
                start_set[n] = n
                end_set[n] = n
                if m == 1:
                    counter += 1
            if counter > 0:
                ans = idx + 1
        return ans
