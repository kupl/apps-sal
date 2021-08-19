(n, m) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
M = [[a[i] & b[j] for j in range(m)] for i in range(n)]
res = 0
M = sorted(M, key=lambda x: min(x), reverse=True)
for x in M:
    res = min([e | res for e in x])
print(res)
