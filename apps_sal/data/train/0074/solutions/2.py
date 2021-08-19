import sys

readline = sys.stdin.readline
read = sys.stdin.read
def ns(): return readline().rstrip()
def ni(): return int(readline().rstrip())
def nm(): return map(int, readline().split())
def nl(): return list(map(int, readline().split()))
def prn(x): return print(*x, sep='\n')


def solve():
    n, k = nm()
    mini = [tuple(nl() + [i + 1]) for i in range(n)]
    mini.sort(key=lambda x: x[1])
    # print(mini)
    dp = [-1] * (k + 1)
    dp[0] = 0
    f = [[0] * (k + 1) for _ in range(n)]
    for i in range(n):
        if dp[k] > 0:
            dp[k] += (k - 1) * mini[i][1]
        for j in range(k - 1, -1, -1):
            if dp[j] >= 0:
                if dp[j + 1] < dp[j] + mini[i][0] + j * mini[i][1]:
                    dp[j + 1] = dp[j] + mini[i][0] + j * mini[i][1]
                    f[i][j + 1] = 1
                dp[j] += (k - 1) * mini[i][1]

    cx = k
    a = list()
    b = list()
    for i in range(n - 1, -1, -1):
        if f[i][cx]:
            a.append(mini[i][2])
            cx -= 1
        else:
            b.append(mini[i][2])
    com = list()
    for x in a[:0:-1]:
        com.append(x)
    for x in b:
        com.append(x)
        com.append(-x)
    com.append(a[0])
    print(len(com))
    print(*com)
    return


T = ni()
for _ in range(T):
    solve()
