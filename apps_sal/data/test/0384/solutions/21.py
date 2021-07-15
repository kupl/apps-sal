n = int(input())
ans = []
cnt = 0
for i in input().strip():
    if (i == 'W' and cnt):
        ans.append(cnt)
        cnt = 0
    elif (i == 'B'):
        cnt += 1
if (cnt):
    ans.append(cnt)
    cnt = 0
print(len(ans))
print(*ans)

