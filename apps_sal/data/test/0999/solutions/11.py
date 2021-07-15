minn = 999999999999
maxn = 0
minm = 999999999999
maxm = 0

for n in range(int(input())):
    l, r = map(int, input().split())
    minn = min(minn, r)
    maxn = max(maxn, l)

for m in range(int(input())):
    l, r = map(int, input().split())
    minm = min(minm, r)
    maxm = max(maxm, l)

print(max([maxm - minn, maxn - minm, 0]))
