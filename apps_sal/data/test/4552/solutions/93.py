N = int(input())
F = [int(input().replace(' ', ''), 2) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]
ans = float('-inf')

for i in range(1, 2**10):
    ans = max(ans, sum(p[bin(i & f).count('1')] for f, p in zip(F, P)))
print(ans)
