def solve(n, c, mem):
    if (n, c) in mem:
        return mem[(n, c)]
    if n == 0:
        res = 1
    elif c == 'a':
        res = solve(n-1, 'e', mem) % (10**9 + 7)
    elif c == 'e':
        res = (solve(n-1, 'a', mem)+solve(n-1, 'i', mem)) % (10**9 + 7)
    elif c == 'i':
        a = solve(n-1, 'a', mem)
        e = solve(n-1, 'e', mem)
        o = solve(n-1, 'o', mem)
        u = solve(n-1, 'u', mem)
        res = (a+e+o+u) % (10**9 + 7)
    elif c == 'o':
        res = (solve(n-1, 'i', mem) + solve(n-1, 'u', mem))% (10**9 + 7)
    else:
        res = solve(n-1, 'a', mem) % (10**9 + 7)
    
    mem[(n, c)] = res
    return res

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mem = {}
        return sum(solve(n-1, c, mem) for c in {'a', 'e', 'i', 'o', 'u'}) % (10**9 + 7)
