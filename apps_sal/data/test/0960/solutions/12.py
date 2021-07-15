# list(map(int, input().split()))
# map(int, input().split())

n, k = map(int, input().split())
if n == 0:
    print(0)
    return

m = 100000000000000000
for i in range(1, k):
    if n % i == 0:
        m = min(m, n // i * k + i)
print(m)
