class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        memo = {}

        def helper(a, b):
            if a == b:
                return 0
            if (a, b) in memo:
                return memo[(a, b)]
            res = float('inf')
            if a[-1] == b[-1]:
                res = min(res, helper(a[:-1], b[:-1]))
            else:
                for i in range(len(a) - 1):
                    if a[i] == b[-1] and a[i] != b[i]:
                        a_new = a[:i] + a[-1] + a[i + 1:-1]
                        res = min(res, 1 + helper(a_new, b[:-1]))
            memo[(a, b)] = res
            return res
        return helper(A, B)
        '''
        def neighbor(x):
            i = 0
            while x[i] == B[i]:  
                i += 1
            for j in range(i + 1, len(x)): 
                if x[j] == B[i]:
                    yield x[:i] + x[j] + x[i + 1:j] + x[i] + x[j + 1:]
        q, seen = [(A, 0)], {A}
        for x, d in q:
            if x == B:
                return d
            for y in neighbor(x):
                if y not in seen:
                    seen.add(y)
                    q.append((y, d + 1))
        '''
