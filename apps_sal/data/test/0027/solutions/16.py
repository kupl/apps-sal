l = int(input())
k = input()
ans = 0
for i in range(1, (l // 2) + 1):
    flag = 1
    for j in range(0, i):
        if k[j] != k[i + j]:
            flag = 0
            break
    if flag == 1:
        ans = max(ans, i)
su = l - (ans)
if ans > 0:
    su += 1
print(su)
