class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        cnt, ans = 0, -1
        start_end, end_start = {}, {}
        for i, n in enumerate(arr, start=1):
            start, end = n, n
            if n-1 in end_start:
                start = end_start[n-1] 
                del end_start[n-1]
                if n-start == m:
                    cnt -= 1
            if n+1 in start_end:
                end = start_end[n+1]
                del start_end[n+1]
                if end-n == m:
                    cnt -= 1
            start_end[start] = end
            end_start[end] = start
            if end-start+1 == m:
                cnt += 1
            if cnt >= 1:
                ans = i
        return ans

