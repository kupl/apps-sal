(n, k) = list(map(int, input().split()))
p = k
for i in range(n - 1):
    p *= k - 1
print(p)
