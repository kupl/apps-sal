import sys


def getInt():
    n = sys.stdin.readline()
    return int(n)


def getStr():
    s = sys.stdin.readline()
    return s


def getArr():
    arr = list(map(int, sys.stdin.readline().split()))
    return arr


def getPair():
    (a, b) = list(map(int, sys.stdin.readline().split()))
    return (a, b)


def put(n):
    sys.stdout.write(str(n) + '\n')


a = getArr()
cc = a[2]
st = []
s = []
ch = [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(101)] for j in range(101)]
for i in range(a[0]):
    c = getArr()
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
for i in range(a[1]):
    ans = 0
    l = getArr()
    i1 = l[1]
    j1 = l[2]
    i2 = l[3]
    j2 = l[4]
    count = [dp[i2 + 1][j2 + 1][k] + dp[i1][j1][k] - dp[i2 + 1][j1][k] - dp[i1][j2 + 1][k] for k in range(11)]
    t = l[0]
    for m in range(11):
        lk = (m + t) % (cc + 1)
        ans += count[m] * lk
    print(ans)
