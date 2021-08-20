n = int(input())
s = input()
x = list(map(int, input().split()))
p = sorted([(x[i], s[i]) for i in range(n)])
ans = -1
mi = 10 ** 10
for i in range(1, n):
    if p[i - 1][1] == 'R' and p[i][1] == 'L' and (p[i][0] - p[i - 1][0] < mi):
        mi = p[i][0] - p[i - 1][0]
        ans = mi // 2
print(ans)
