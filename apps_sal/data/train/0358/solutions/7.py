class Solution:

    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        idx_og = 0
        idx_res = 0
        res = S
        for (index, source, target) in sorted(zip(indexes, sources, targets)):
            if S[index:index + len(source)] == source:
                index2 = index - idx_og + idx_res
                res = res[:index2] + target + res[index2 + len(source):]
                idx_og = index + len(source)
                idx_res = index2 + len(target)
        return res
