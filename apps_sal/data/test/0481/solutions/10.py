(n, x) = map(int, input().split())
k = 0
for i in range(1, n + 1):
    if x % i == 0 and x // i <= n:
        k += 1
print(k)
