import itertools as it
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
if sum(a) % 2:
    print('NO')
else:
    f = False
    q = it.product([-1, 1], repeat=n)
    for i in q:
        s = 0
        for j in range(len(i)):
            s += i[j] * a[j]
        if s % 360 == 0:
            f = True
            break
    if f:
        print("YES")
    else:
        print("NO")
