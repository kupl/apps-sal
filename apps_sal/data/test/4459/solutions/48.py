N = int(input())
a = list(map(int, input().split()))

a = sorted(a)
l = a[0]
cnt = 0

b = []
for i in range(N):
    if a[i] == l:
        cnt += 1
    else:
        b.append([l, cnt])
        l = a[i]
        cnt = 1
if cnt > 0:
    b.append([l, cnt])

ans = 0
for i in range(len(b)):
    if b[i][0] > b[i][1]:
        ans += b[i][1]
    else:
        ans += b[i][1] - b[i][0]

print(ans)
