n = int(input())
p = 0
a = []
for _ in range(n):
    x, k = list(map(int, input().split()))
    while k > len(a):
        a.append(-1)
    k = k - 1
    if a[k] < x - 1:
        print('NO')
        return
    else:
        a[k] = max(x, a[k])
print('YES')
