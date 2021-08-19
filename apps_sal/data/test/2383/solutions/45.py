n = int(input())
arr = list(map(int, input().split()))
i = 1
cnt = 0
for char in arr:
    if char == i:
        i += 1
    else:
        cnt += 1
if i == 1:
    print(-1)
else:
    print(cnt)
