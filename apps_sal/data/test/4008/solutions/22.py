(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
s = list(set(a))
m = [0] * 5005
k1 = []
for i in range(n):
    k1.append([a[i], i])
k1.sort()
ans = [0] * n
for i in a:
    m[i] += 1
f = 0
for i in s:
    if m[i] > k:
        f = 1
if f == 1:
    print('NO')
else:
    j = 0
    print('YES')
    for i in range(n):
        ans[k1[i][1]] = i % k + 1
    print(*ans)
