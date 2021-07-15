#[] Greedy
#O(NlogN)
BEGIN, END = 0, 1
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        stitch = max_reach = cnt = i = 0
        clips = sorted((i-diff, i+diff) for i, diff in enumerate(ranges) if diff) #sort by start
        N = len(clips)
        while max_reach < n: #NOTE: WA: max_reach < `n` instead of `N`
            #try to find furthest end-point
            while i < N and clips[i][BEGIN] <= stitch:
                max_reach = max(max_reach, clips[i][END])
                i += 1
            if stitch == max_reach:
                return -1 #unable to reach n
            cnt += 1
            stitch = max_reach #put clips[i] into solution and extend the next end-point
        return cnt
