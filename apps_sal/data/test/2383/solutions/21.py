n = int(input())
a = list(map(int, input().split()))

ans = 0
cnt = 0
for i in a:
    if i == cnt + 1:
        cnt += 1
    else:
        ans += 1
print(ans if cnt else -1)
