n = int(input())
num = list(map(int, input().split()))
cnt = 1
ans = 0
if 1 not in num:
    print(-1)
    return
for i in range(n):
    if num[i] == cnt:
        cnt += 1
    else:
        ans += 1
print(ans)
