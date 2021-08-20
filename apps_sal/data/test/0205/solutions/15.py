(n, b) = map(int, input().split())
fac = []
i = 2
while i * i <= b:
    if b % i == 0:
        fac.append([i, 0])
        while b % i == 0:
            fac[-1][1] += 1
            b //= i
    i += 1
if b > 1:
    fac.append([b, 1])
ans = int(1e+20)
for i in fac:
    cnt = 0
    x = i[0]
    while x <= n:
        cnt += n // x
        x *= i[0]
    ans = min(ans, cnt // i[1])
print(ans)
