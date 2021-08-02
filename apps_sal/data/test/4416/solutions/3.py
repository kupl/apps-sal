
n, k = list(map(int, input().split(" ")))
db = []
a = []
b = []
for i in range(n):
    t, A, B = list(map(int, input().split(" ")))
    if A == B == 1:
        db.append(t)
    elif A == 1:
        a.append(t)
    elif B == 1:
        b.append(t)
a.sort()
b.sort()
for i in range(min(len(a), len(b))):
    db.append((a[i] + b[i]))
if len(db) < k:
    print(-1)
else:
    db.sort()
    print(sum(db[:k]))
