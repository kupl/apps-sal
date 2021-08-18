class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        start = {}
        end = {}
        groups = collections.defaultdict(set)
        ans = -1
        for idx, a in enumerate(arr):
            new_start, new_end = a, a
            if a + 1 in start:
                new_end = start[a + 1]
                del start[a + 1]
                groups[new_end - (a + 1) + 1].remove((a + 1, new_end))
            if a - 1 in end:
                new_start = end[a - 1]
                del end[a - 1]
                groups[a - 1 - new_start + 1].remove((new_start, a - 1))
            start[new_start] = new_end
            end[new_end] = new_start
            groups[new_end - new_start + 1].add((new_start, new_end))
            if len(groups[m]) > 0:
                ans = idx + 1
        return ans
