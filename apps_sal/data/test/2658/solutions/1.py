(n, k) = map(int, input().split())
a = list(map(int, input().split()))
b = [False] * n
pos = 0
for i in range(min(n, k)):
    if b[pos] != False:
        loop = i - b[pos] + 1
        break
    b[pos] = i + 1
    pos = a[pos] - 1
    k -= 1
if k > 0:
    for i in range(k % loop):
        pos = a[pos] - 1
print(pos + 1)
