n, m, k = list(map(int, input().split()))
x = [list([int(a) - 1 for a in input().split()]) for i in range(n)]
res = [-1] * n
locked = [False] * k
for t in range(m):
    w = [0] * k
    for i in range(n):
        if res[i] == -1 and x[i][t] != -1:
            w[x[i][t]] += 1

    for i in range(n):
        if res[i] == -1 and x[i][t] != -1 and (w[x[i][t]] >= 2 or locked[x[i][t]]):
            locked[x[i][t]] = True
            res[i] = t
res = [i + 1 for i in res]
for i in res:
    print(i)

