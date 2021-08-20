def stp(f):
    q = 1
    for i in range(f):
        q *= 2
    return q


def opr(n):
    q = 1
    counter = 0
    while q != n:
        q *= 2
        counter += 1
    return counter


n = int(input())
S = list(map(int, input().split()))
st = 1
counter = 1
while st < n:
    st *= 2
    counter += 1
if st != n:
    st // 2
    counter -= 1
dp = [[] for i in range(counter)]
for i in range(n):
    dp[0].append([0, S[i]])
for i in range(1, counter):
    chislo = stp(i)
    for l in range(n - chislo + 1):
        r = l + chislo
        dp[i].append([dp[i - 1][l][0] + dp[i - 1][l + chislo // 2][0], (dp[i - 1][l][1] + dp[i - 1][l + chislo // 2][1]) % 10])
        if dp[i - 1][l][1] + dp[i - 1][l + chislo // 2][1] > 9:
            dp[i][l][0] += 1
q = int(input())
for i in range(q):
    (a, b) = map(int, input().split())
    w = b - a + 1
    counter = opr(w)
    print(dp[counter][a - 1][0])
