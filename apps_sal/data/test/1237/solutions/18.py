n, s = map(int, input().split())
maxSmt = 0
for i in range(n):
    f, t = map(int, input().split())
    maxSmt = max(maxSmt, max(t - (s - f), 0))
print(s + maxSmt)
