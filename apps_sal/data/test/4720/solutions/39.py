
n = int(input())
men = []
for i in range(n):
    l, r = map(int, input().split())
    men.append([l, r])
ans = 0

for i in range(n):
    ans += men[i][1] - men[i][0] + 1

print(ans)
