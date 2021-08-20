(n, k) = map(int, input().split())
val = 0
for i in range(n):
    (l, r) = map(int, input().split())
    val += r - l + 1
print((k - val % k) % k)
