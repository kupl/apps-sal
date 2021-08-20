class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        mcount = 0
        lastindex = -1
        ends = {}
        starts = {}
        for i in range(n):
            index = arr[i]
            if index - 1 in ends and index + 1 in starts:
                start = ends[index - 1]
                end = starts[index + 1]
                old1 = index - start
                old2 = end - index
                if old1 == m:
                    mcount -= 1
                if old2 == m:
                    mcount -= 1
                if end - start + 1 == m:
                    mcount += 1
                (starts[start], ends[end]) = (end, start)
                starts.pop(index + 1)
                ends.pop(index - 1)
            elif index - 1 in ends:
                start = ends[index - 1]
                old1 = index - start
                if old1 == m:
                    mcount -= 1
                elif old1 == m - 1:
                    mcount += 1
                starts[start] = index
                ends[index] = start
                ends.pop(index - 1)
            elif index + 1 in starts:
                end = starts[index + 1]
                old1 = end - index
                if old1 == m:
                    mcount -= 1
                elif old1 == m - 1:
                    mcount += 1
                starts[index] = end
                ends[end] = index
                starts.pop(index + 1)
            else:
                starts[index] = index
                ends[index] = index
                if m == 1:
                    mcount += 1
            if mcount != 0:
                lastindex = i + 1
        return lastindex
