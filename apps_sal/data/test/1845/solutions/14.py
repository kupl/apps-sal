def factors(a):
    f = []
    for i in range(2, a):
        if a % i == 0:
            f.append(i)
    return f


n = int(input())
a = list(map(int, input().split()))
a.sort()
sm = sum(a)
ans = sm
i = n - 1
while i > 0:
    f = factors(a[i])
    if f:
        for j in f:
            x, y = a[i] // j, a[0] * j
            ans = min(ans, sm - a[i] - a[0] + x + y)
    i -= 1
print(ans)
