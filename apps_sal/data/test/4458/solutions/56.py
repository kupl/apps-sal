n = int(input())
p = list(map(int, input().split()))
ans = 1
cur_min = p[0]
for i in range(1, n):
    cur_min = min(p[i - 1], cur_min)
    if p[i] <= cur_min:
        ans += 1
print(ans)
