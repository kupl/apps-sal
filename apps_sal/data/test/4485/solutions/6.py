import collections

n, m = list(map(int, input().split()))
a, b, c = [], [], []
for i in range(m):
    A = list(map(int, input().split()))
    a.append(A)
for i in range(m):
    if a[i][1] == n:
        b.append(a[i][0])
    elif a[i][0] == 1:
        c.append(a[i][1])
if len(set(b) & set(c)) > 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
