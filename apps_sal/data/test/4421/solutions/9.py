n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
d = [0] * k
for i in range(n):
    d[a[i] % k] += 1

num = 0
for i in range(k):
    if k - i < i:
        break
    if i == 0:
        num += d[i] // 2
    elif i == k - i:
        num += d[i] // 2
    else:
        num += min(d[i], d[k - i])

print(num * 2)

