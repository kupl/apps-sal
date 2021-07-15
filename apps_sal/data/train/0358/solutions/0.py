class Solution:
    def findReplaceString(self, s: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        l = []
        for i, tgt, rpl in zip(indexes, sources, targets):
            if s[i:i + len(tgt)] == tgt:
                l.append((i, tgt, rpl))
        l.sort()
        j = 0
        s = list(s)
        for i, tgt, rpl in l:
            s[i + j:i + j + len(tgt)] = rpl
            j += len(rpl) - len(tgt)
        return ''.join(s)
