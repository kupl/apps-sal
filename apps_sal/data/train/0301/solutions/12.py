def longest_substr(A, B, i, j, cache):
    if i == len(A) or j == len(B):
        return 0
    
    res = cache.get(i, {}).get(j, None)
    if res is not None:
        return res
    
    length1 = 0
    if A[i] == B[j]:
        length1 = 1 + longest_substr(A, B, i + 1, j + 1, cache)
    length2 = longest_substr(A, B, i + 1, j, cache)
    length3 = longest_substr(A, B, i, j + 1, cache)
    
    length = max(length1, length2, length3)
    cache[i][j] = length
    return length
        


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        cache = defaultdict(dict)
        return longest_substr(A, B, 0, 0, cache)
