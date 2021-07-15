n, k = list(map(int, input().split()))
for i in range(k - 1, 0, -1):
    if n % i == 0:
        r = i
        break
n //= r
print(n * k + r)

