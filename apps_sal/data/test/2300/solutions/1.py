

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

for i in range(m):
    t, l, r = list(map(int, input().split()))
    if t == 1:
        a[l-1] = r
    else:
        s = 0
        fiba = fibb = 1
        for i in range(l-1, r):
            s += fiba * a[i]
            fiba, fibb = fibb, fiba + fibb
        print(s % 1000000000)

