class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        '''
        maintain a DS to record all segments (start, end).
        For each arr[i], test if i-1 or i+1 are in the DS.
        If so, merge the interval and insert to the DS again.

        DS:
        - Insert interval
        - Delete interval
        '''

        starts = {}
        ends = {}
        intervals = {}
        interval_count = 0

        ans = -1

        for i, x in enumerate(arr):
            s, e = x, x
            if x - 1 in ends:
                iid = ends[x - 1]
                s = intervals[iid][0]
                if intervals[iid][1] - intervals[iid][0] + 1 == m:
                    ans = max(ans, i)
                del starts[intervals[iid][0]]
                del ends[intervals[iid][1]]
            if x + 1 in starts:
                iid = starts[x + 1]
                e = intervals[iid][1]
                if intervals[iid][1] - intervals[iid][0] + 1 == m:
                    ans = max(ans, i)
                del starts[intervals[iid][0]]
                del ends[intervals[iid][1]]
            iid = interval_count
            interval_count += 1
            intervals[iid] = (s, e)
            starts[s] = iid
            ends[e] = iid
            if e - s + 1 == m:
                ans = max(ans, i + 1)

        return ans
