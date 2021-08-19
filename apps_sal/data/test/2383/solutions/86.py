n = int(input())
ai = list(map(int, input().split()))
tmp = 1
ans = 0
for i in range(n):
    if ai[i] == tmp:
        tmp += 1
    else:
        ans += 1
if tmp == 1:
    ans = -1
print(ans)
