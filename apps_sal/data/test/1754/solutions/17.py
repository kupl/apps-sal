n, m, k = list(map(int, input().split()))
ps = list(map(int, input().split()))

schs = [list() for _ in range(m)]
ss = list(map(int, input().split()))
for i in range(n):
    schs[ss[i] - 1].append((ps[i], i))
for j in range(m):
    schs[j].sort()

n = 0
cs = list(map(int, input().split()))
for c in cs:
    c -= 1
    if schs[ss[c] - 1][-1][1] != c:
        n += 1

print(n)
