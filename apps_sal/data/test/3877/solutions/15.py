(n, l, r) = map(int, input().split())
s = ''
a = []
k = n
while k > 1:
    a.append(k % 2)
    k = k // 2
a.append(k)
ans = 0
for i in range(l - 1, r):
    s = '0' + bin(i)[2:]
    cur = 1
    while s[-cur] != '0':
        cur += 1
    ans += a[-cur]
print(ans)
