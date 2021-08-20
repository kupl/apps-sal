class Solution:

    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        S = list(S)
        for (i, s, t) in sorted(zip(indexes, sources, targets), reverse=True):
            appl = all([i + ind < len(S) and S[i + ind] == s[ind] for ind in range(len(s))])
            if appl:
                S[i:i + len(s)] = list(t)
        return ''.join(S)
