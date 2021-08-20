n = int(input())
x = list(map(int, input().split()))
y = sorted(x)
(t, w) = (y[n // 2 - 1], y[n // 2])
for i in range(n):
    if x[i] < w:
        print(w)
    else:
        print(t)
