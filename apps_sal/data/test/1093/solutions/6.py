n, m = list(map(int, input().split()))
pole = []
for i in range(n):
    s = input()
    pole.append(s)
ans = []
for j in range(m):
    for i in range(n):
        if pole[i][j] == '*':
            ans.append(n - i)
            break
ans2 = 0
ans1 = 0
newans = []
newans.append(ans[0])
for i in ans:
    newans.append(i)
newans.append(ans[-1])
for i in range(1, m + 1):
    ans1 = max(ans1, newans[i] - newans[i - 1])
    ans2 = max(ans2, newans[i] - newans[i + 1])
print(ans1, ans2)

