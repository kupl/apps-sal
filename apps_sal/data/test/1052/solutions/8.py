"""
while 1:
    n, k = map(int, input().split())
    
    def solve(n, k):
        from itertools import permutations
        res = 0
        for p in permutations([i for i in range(n)]):
            c = sum(i == p[i] for i in range(n))
            if c >= n - k: res += 1
        return res
    
    print(solve(n, k))
"""
(n, k) = map(int, input().split())
ans = 1
if k >= 2:
    ans += n * (n - 1) // 2
if k >= 3:
    ans += n * (n - 1) * (n - 2) // 3
if k >= 4:
    ans += n * (n - 1) * (n - 2) * (n - 3) // 24 * 9
print(ans)
