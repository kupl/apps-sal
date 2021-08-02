n, d = list(map(int, input().split()))
x = [0] * n
for i in range(n):
    x[i] = list(map(int, input().split()))


def f(i):
    return (i**0.5 - int(i**0.5)) == 0.0


ans = 0
for i in range(n):
    for j in range(i + 1, n):
        dist = 0
        for k in range(d):
            dist += (x[i][k] - x[j][k])**2
        ans += 1 if f(dist) else 0
print(ans)
