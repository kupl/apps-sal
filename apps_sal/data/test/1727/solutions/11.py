n = int(input())
inp = [[int(x) for x in input().split()] for i in range(n)]
ans = 0
least = 0
for i in range(0, n):
    if i == 0 or least < inp[i][0] - inp[i][1]:
        ans += 1
        least = inp[i][0]
    elif i == n - 1 or (i + 1 < n and inp[i][0] + inp[i][1] < inp[i + 1][0]):
        least = inp[i][0] + inp[i][1]
        ans += 1
    else:
        least = inp[i][0]
print(ans)
