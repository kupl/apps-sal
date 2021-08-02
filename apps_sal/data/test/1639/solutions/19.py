n = int(input())
al = list(map(int, input().split()))
res, t = 0, 0
last = -1
for i in al:
    if i >= last:
        t += 1
    else:
        res = max(t, res)
        t = 1
    last = i
print(max(t, res))
