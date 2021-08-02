n, x = map(int, input().split())
l = list(map(int, input().split()))
ans = 0
cnt = 1
for i in l:
    ans += i
    if ans > x:
        break
    cnt += 1

print(cnt)
