class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # get group's key and length, e.g. 'aaabaa' -> [[a, 3], [b, 1], [a, 3]]
        # itertools.groupby function returns consecutive keys and groups from the iterable.
        # note itertools.groupby(iterable, key_func) supports lambda function
        # If the key function is not specified or is None, key defaults to an identity function and returns the element unchanged.
        A = [[c, len(list(g))] for c, g in itertools.groupby(text)]
        # use count dict as upper bound 'aaabaa' -> {a: 6, b: 1}
        count = collections.Counter(text)
        # case 1: extend 1 more, use min here to avoid the case that there's no extra char to extend
        res = max(min(k + 1, count[c]) for c, k in A)
        # case 2: merge 2 groups together with 1 char in between
        for i in range(1, len(A) - 1):
            if A[i][1] == 1 and A[i - 1][0] == A[i + 1][0]:
                res = max(res, min(A[i - 1][1] + 1 + A[i + 1][1], count[A[i - 1][0]]))
        return res
        
        

