import sys
a = [int(i) for i in sys.stdin.readline().split()]
cc = a[2]
st = []
s = []
ch = [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(101)] for j in range(101)]
for i in range(a[0]):
    c = [int(j) for j in sys.stdin.readline().split()]
    st.append((c[0], c[1]))
    s.append(c[2])
    ch[c[0]][c[1]][c[2]] += 1
dp = [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(102)] for j in range(102)]
for i in range(1, 102):
    for j in range(1, 102):
        for k in range(11):
            dp[i][j][k] = dp[i - 1][j][k] + dp[i][j - 1][k] - dp[i - 1][j - 1][k]
        for k in range(11):
            dp[i][j][k] += ch[i - 1][j - 1][k]
anss = []
for i in range(a[1]):
    ans = 0
    l = [int(j) for j in sys.stdin.readline().split()]
    pp = l[0]
    i1 = l[1]
    j1 = l[2]
    i2 = l[3]
    j2 = l[4]
    count = [dp[i2 + 1][j2 + 1][k] + dp[i1][j1][k] - dp[i2 + 1][j1][k] - dp[i1][j2 + 1][k] for k in range(11)]
    t = l[0]
    for m in range(11):
        lk = (m + t) % (cc + 1)
        ans += count[m] * lk
    anss.append(str(ans))
print('\n'.join(anss))
