class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        for i, s, t in sorted(zip(indexes, sources, targets), reverse=True):
            if S[i:i + len(s)] == s:
                S = S[:i] + t + S[i + len(s):]
        return S
