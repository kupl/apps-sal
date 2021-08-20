(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
t = 0
result = 0
for i in range(0, k):
    t += a[i]
    result += a[i]
index = 0
for i in range(k, n):
    t += a[i]
    t -= a[i - k]
    if result > t:
        result = t
        index = i - k + 1
print(index + 1)
