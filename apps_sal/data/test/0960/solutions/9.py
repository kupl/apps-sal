(n, k) = list(map(int, input().split()))
ans = 10 ** 18
for i in range(1, k):
    if n % i > 0:
        continue
    mod = i
    div = n // mod
    x = div * k + mod
    if x < ans:
        ans = x
print(ans)
