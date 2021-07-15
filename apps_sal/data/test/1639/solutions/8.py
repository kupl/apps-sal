n = int(input())
ans = 0
cnt = 0
last = 0
for i in map(int, input().split()):
    if i >= last:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1
    last = i
ans = max(ans, cnt)
print(ans)

