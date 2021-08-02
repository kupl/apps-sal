k = int(input())
a = [list(input()) for i in range(4)]
x = [0 for i in range(10)]
for i in range(4):
    for j in range(4):
        if a[i][j] == '.': continue
        n = int(a[i][j])
        x[n] += 1
ok = True
for i in range(10):
    if x[i] > 2 * k:
        ok = False
if (ok):
    print("YES")
else:
    print("NO")
