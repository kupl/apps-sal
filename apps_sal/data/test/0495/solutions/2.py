(a1, K) = map(int, input().split())
a = []
while a1 != 0:
    a.append(a1 % 10)
    a1 //= 10
n = len(a)
k = n
while 1:
    if k == 0:
        break
    ma = 0
    for i in range(max(0, k - 1 - K), k):
        if ma <= a[i]:
            ma = a[i]
            pos = i
    if ma == a[k - 1]:
        k -= 1
        continue
    while K != 0 and pos + 1 < n and (a[pos + 1] < a[pos]):
        (a[pos], a[pos + 1]) = (a[pos + 1], a[pos])
        pos += 1
        K -= 1
    if K == 0:
        break
    k -= 1
for i in range(n):
    print(a[n - i - 1], end='')
