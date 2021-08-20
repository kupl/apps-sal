(n, x) = map(int, input().split())
l = 0
for i in range(1, n + 1):
    if x % i == 0 and x // i <= n:
        l += 1
print(l)
