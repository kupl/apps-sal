"""import sys
sys.stdin = open("in", "r")"""
(n, w) = map(int, input().split())
arr = [[i, int(x)] for (i, x) in enumerate(input().split())]
arr.sort(reverse=True, key=lambda a: a[1])
res = []
pos = True
for a in arr:
    if w <= 0:
        pos = False
        break
    res.append([a[0], (a[1] + 1) // 2])
    w -= (a[1] + 1) // 2
while w > 0:
    for i in range(n):
        ex = min(w, arr[i][1] - res[i][1])
        w -= ex
        res[i][1] += ex
        if w == 0:
            break
res.sort(key=lambda a: a[0])
if pos:
    print(' '.join(map(lambda a: str(a[1]), res)))
else:
    print(-1)
