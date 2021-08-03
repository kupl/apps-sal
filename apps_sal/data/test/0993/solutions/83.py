import collections

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

c = collections.Counter()

ans = 0
s = 0
c[0] += 1
for a in A:
    s += a
    s %= M
    ans += c[s]
    c[s] += 1

print(ans)
