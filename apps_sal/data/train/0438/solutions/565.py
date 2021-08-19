class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        start = {}
        end = {}
        lengths = {}
        ans = -1
        for i in range(len(arr)):
            st = arr[i]
            ending = st + 1
            if st in end:
                tempStart = st
                st = end[st]
                end.pop(st, None)
            else:
                tempStart = st
            if ending in start:
                ed = ending
                ending = start[ending]
                start.pop(ed, None)
            else:
                ed = ending
            if st != tempStart:
                lengths[tempStart - st] -= 1
            if ed != ending:
                print('d')
                lengths[ending - ed] -= 1
            if ending - st not in lengths:
                lengths[ending - st] = 1
            else:
                lengths[ending - st] = lengths[ending - st] + 1
            start[st] = ending
            end[ending] = st
            if m in lengths and lengths[m] > 0:
                ans = i + 1
        return ans
