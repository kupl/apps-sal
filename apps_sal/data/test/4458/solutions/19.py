n = int(input())
pl = list(map(int, input().split()))

min_num = 1001001001
ans = 0
for p in pl:
    if p <= min_num:
        ans += 1
        min_num = p

print(ans)
