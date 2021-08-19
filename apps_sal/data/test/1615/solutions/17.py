(n, k) = list(map(int, input().split()))
res = 0
for i in range(n):
    (start, end) = list(map(int, input().split()))
    res += end - start + 1
print(0 if not res % k else k - res % k)
