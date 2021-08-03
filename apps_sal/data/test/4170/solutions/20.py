n = int(input())
l = list(map(int, input().split()))
ans = [0]
cnt = 0
for i in range(n - 1):
    if l[i] >= l[i + 1]:
        cnt += 1
    else:
        if cnt > 0:
            ans.append(cnt)
        cnt = 0

ans.append(cnt)
print(max(ans))
