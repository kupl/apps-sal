import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
poss = True
col = []
row = []
cl = None
t = 0
ts = []
i = n - 1
while i >= 0:
    if a[i] == 1:
        col.append(i)
        row.append(i)
        t += 1
        ts.append([i + 1, i + 1])
    if a[i] == 2:
        if len(col) == 0:
            poss = False
        else:
            t += 1
            r = row.pop()
            c = col.pop()
            ts.append([r + 1, i + 1])
            cl = i
    if a[i] == 3:
        if cl != None:
            t += 2
            ts.append([i + 1, i + 1])
            ts.append([i + 1, cl + 1])
            cl = i
        elif len(col) == 0:
            poss = False
        else:
            c = col.pop()
            r = row.pop()
            t += 2
            ts.append([i + 1, i + 1])
            ts.append([i + 1, c + 1])
            cl = i
    i -= 1
if poss:
    print(t)
    for x in ts:
        print(*x)
else:
    print(-1)
