n = int(input())
(x, y) = ([0] * n, [0] * n)
for i in range(n):
    (x[i], y[i]) = map(int, input().split())
ans = [0] * 100001
for elm in x:
    ans[elm] += 1
for elm in y:
    print(n - 1 + ans[elm], n - 1 - ans[elm])
