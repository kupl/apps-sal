(n, k) = map(int, input().split())
mn = int(1e+20)
for i in range(1, k):
    if not n % i:
        mn = min(mn, k * (n // i) + i)
print(mn)
