n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
tmp = {}
for i in range(n):
    x = a[i] - i * k
    if x > 0:
        tmp[x] = tmp.get(x, 0) + 1
x = max(tmp, key = lambda x: tmp[x])
print(n - tmp[x])
if tmp[x] == n:
    return
for i in range(n):
    if x + i * k > a[i]:
        print('+', i + 1, x + i * k - a[i])
    elif x + i * k < a[i]:
        print('-', i + 1, a[i] - i * k - x)

