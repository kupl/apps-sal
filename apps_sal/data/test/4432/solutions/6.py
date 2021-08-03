from sys import stdin
input = stdin.readline
t = int(input())
for rew in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    wyn = 0
    listka = []
    cur = [l[0]]
    for i in range(1, n):
        if cur and l[i] * cur[-1] < 0:
            listka.append(cur)
            cur = [l[i]]
        else:
            cur.append(l[i])
    listka.append(cur)
    for i in listka:
        wyn += max(i)
    print(wyn)
