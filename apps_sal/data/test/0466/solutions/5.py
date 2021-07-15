c, d = list(map(int, input().split()))
n, m = list(map(int, input().split()))
k = int(input())

s = max(n * m - k, 0)
res = 0
while s:
    if c > min(s, n) * d:
        res += min(s,n) * d
    else:
        res += c
    s -= min(s,n)
print(res)

