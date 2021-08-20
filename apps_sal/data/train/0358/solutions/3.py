class Solution:

    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        (result, offset) = (S, 0)
        for (i, s, t) in sorted(zip(indexes, sources, targets)):
            if S[i:i + len(s)] == s:
                result = result[:offset + i] + t + result[offset + i + len(s):]
                offset += len(t) - len(s)
        return result
