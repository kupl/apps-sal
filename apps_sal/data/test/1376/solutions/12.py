
n = int(input())

arr = list(map(int, input().strip().split()))

ans = [[] for i in range(n)]

for i in range(2 * n):
    ans[arr[i] - 1].append(i)

an = 0
for i in range(n):
    if i == 0:
        an += ans[i][0] + ans[i][1]
    else:
        v1 = abs(ans[i][0] - ans[i - 1][0]) + abs(ans[i][1] - ans[i - 1][1])
        v2 = abs(ans[i][0] - ans[i - 1][1]) + abs(ans[i][1] - ans[i - 1][0])
        an += min(v1, v2)
print(an)
