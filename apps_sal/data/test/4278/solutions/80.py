import collections
N = int(input())
s = [''.join(sorted(input())) for _ in range(N)]
c = collections.Counter(s)
ans = 0
for si in set(s):
    n = c[si]
    ans += n * (n - 1) // 2
print(ans)
