n = int(input())
cnt = 0
ans = 0
for i in list(map(int, input().split())) + [1]:
    if i < 4:
        ans += cnt // 3
        cnt = 0
    else:
        cnt += 1
print(ans)
