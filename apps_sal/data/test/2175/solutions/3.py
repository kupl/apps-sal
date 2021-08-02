def command(cmd):
    t = cmd[0]
    if t == 1:
        pour(cmd[1], cmd[2])
    else:
        amount(cmd[1])


def pour(p, amount):
    Skip = []
    while p <= n and amount > 0:
        t = C[p - 1] - W[p - 1]
        if amount >= t:
            amount -= t
            W[p - 1] = C[p - 1]
            Skip.append(p)
        else:
            W[p - 1] += amount
            break
        p = Links[p]
    for i in Skip:
        Links[i] = p
        # print(W)


def amount(p):
    P.append(W[p - 1])


n = int(input())
C = list(map(int, input().split()))
W = [0] * n
Links = list(map(int, range(1, n + 2)))
P = []
m = int(input())
for i in range(m):
    command([int(i) for i in input().split()])
for i in P:
    print(i)
