n, m = list(map(int, input().split()))
k  = n // 2 + n % 2
l = n % 2
while k % m != 0 and l <= n:
    k += 1
    l += 2
print(k if k % m == 0 and k <= n else -1)

