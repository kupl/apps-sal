n = int(input())
al = list(map(int, input().split()))
al.sort()
al.append(-1)
cnt = 1
bl = []
for i in range(n):
    if al[i] == al[i + 1]:
        cnt += 1
    else:
        bl.append([al[i], cnt])
        cnt = 1
tmp = 0
ans = 0
for j in range(len(bl)):
    tmp = bl[j][1]
    if bl[j - 1][0] + 1 == bl[j][0]:
        tmp += bl[j - 1][1]
    if j != len(bl) - 1 and bl[j][0] == bl[j + 1][0] - 1:
        tmp += bl[j + 1][1]

    if tmp > ans:
        ans = tmp

print(ans)
