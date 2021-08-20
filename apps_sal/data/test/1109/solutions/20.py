(n, k) = map(int, input().split())
(a, val) = (list(map(int, input().split())), 0)
for i in range(k):
    c = sum((a[i + j * k] == 1 for j in range(n // k)))
    val += min(c, n // k - c)
print(val)
