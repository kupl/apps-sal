class Solution:

    def lastSubstring(self, s: str) -> str:
        max_ord = max([ord(c) for c in s])
        max_ord_idxs = [i for i in range(len(s)) if ord(s[i]) == max_ord]
        print(max_ord_idxs)
        first_unique_idx = [i for i in range(len(max_ord_idxs) - 1, -1, -1) if i == 0 or max_ord_idxs[i] - 1 != max_ord_idxs[i - 1]]
        print(first_unique_idx)
        max_ord_idxs = [max_ord_idxs[i] for i in first_unique_idx]

        def findNextMaxOrd(cur_idxs, level):
            nextOrd2CurIdx = collections.defaultdict(list)
            hist_max = float('-inf')
            for idx in cur_idxs:
                if idx < len(s) - level:
                    nextOrd2CurIdx[ord(s[idx + level])].append(idx)
                    hist_max = max(hist_max, ord(s[idx + level]))
            return (nextOrd2CurIdx, hist_max)
        level = 1
        while 1:
            if len(max_ord_idxs) == 1:
                return s[max_ord_idxs[0]:]
            (nextOrd2CurIdx, hist_max) = findNextMaxOrd(max_ord_idxs, level)
            if len(nextOrd2CurIdx[hist_max]) == 1:
                return s[nextOrd2CurIdx[hist_max][0]:]
            else:
                max_ord_idxs = nextOrd2CurIdx[hist_max]
                level += 1
