n = 2 * int(input())
w = sorted(map(int, input().split()))
r = 10000
for i in range(n):
    wi = w.pop(i)
    for j in range(i):
        wj = w.pop(j)
        d = [w[i + 1] - w[i] for i in range(0, n - 3, 2)]
        r = min(r, sum(d))
        w.insert(j, wj)
    w.insert(i, wi)
print(r)
