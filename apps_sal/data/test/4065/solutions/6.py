n = int(input())
lst = list(map(int, input().split()))
ans = 1
cnt = 1
for i in range(1, n):
    if lst[i] <= lst[i - 1] * 2:
        cnt += 1
        if cnt > ans:
            ans = cnt
    else:
        cnt = 1
print(ans)

