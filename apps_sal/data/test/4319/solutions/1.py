n = int(input())
a = list(map(int, input().split()))
ans = []
cnt = 0
for i in range(n):
    if a[i] == 1:
        if cnt != 0:
            ans.append(cnt)
            cnt = 0
    cnt += 1
ans.append(cnt)
print(len(ans))
print(*ans)
