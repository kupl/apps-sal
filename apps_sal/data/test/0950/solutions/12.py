n, m = map(int, input().split())
a = ['*', '&', '#']
ans0 = [(10**9, -1)] * n
ans1 = [(10**9, -1)] * n
ans2 = [(10**9, -1)] * n
for i in range(n):
    s = input()
    for j in range(m):
        if s[j] in a:
            ans0[i] = min(ans0[i], (j, i), (m - j, i))
        elif '0' <= s[j] <= '9':
            ans1[i] = min(ans1[i], (j, i), (m - j, i))
        else:
            ans2[i] = min(ans2[i], (j, i), (m - j, i))
ans0.sort()
ans1.sort()
ans2.sort()
ans = 10**5

for i in range(3):
    for j in range(3):
        for k in range(3):
            if ans0[i][1] != ans1[j][1] and ans0[i][1] != ans2[k][1] and ans1[j][1] != ans2[k][1]:
                ans = min(ans, ans0[i][0] + ans1[j][0] + ans2[k][0])
print(ans)
