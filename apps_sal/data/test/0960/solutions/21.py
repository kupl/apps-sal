n, k = list(map(int, input().split()))
deli = []

oti = 1
for i in range(k - 1, 0, -1):
    if n % i == 0:
        oti = i
        break

ans = (n // oti) * k + oti
print(ans)
