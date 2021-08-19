n, m = list(map(int, input().split()))
ab = [list(map(int, input().split())) for i in range(m)]

ab = sorted(ab, key=lambda x: (x[0], x[1]), reverse=True)
# print(ab)
now = 10**5 + 1

preb = -1
ans = 0
for i in range(m):
    if ab[i][1] == preb:
        continue
    if ab[i][1] <= now:
        now = ab[i][0]
        preb = ab[i][1]
        ans += 1
        # print("now",now)
print(ans)
