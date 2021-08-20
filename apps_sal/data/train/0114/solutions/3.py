from sys import stdin
input = stdin.readline
q = int(input())
for rew in range(q):
    n = int(input())
    monster = list(map(int, input().split()))
    m = int(input())
    rycerz = [list(map(int, input().split())) for i in range(m)]
    rycerz.sort()
    rycerz.reverse()
    p = [a[0] for a in rycerz]
    s = [a[1] for a in rycerz]
    maxendu = [-1] * m
    maxendu[0] = s[0]
    if max(p) < max(monster):
        print(-1)
    else:
        for i in range(1, m):
            maxendu[i] = max(maxendu[i - 1], s[i])
        days = 0
        poz = 0
        while True:
            if poz >= n:
                print(days)
                break
            best_potwor = -1
            kroki = 0
            while True:
                if poz + kroki >= n:
                    break
                best_potwor = max(monster[poz + kroki], best_potwor)
                l = 0
                pr = m - 1
                while abs(pr - l) > 0:
                    sr = (l + pr + 1) // 2
                    if p[sr] >= best_potwor:
                        l = sr
                    else:
                        pr = sr - 1
                sr = (pr + l) // 2
                if maxendu[sr] >= kroki + 1:
                    kroki += 1
                else:
                    kroki -= 1
                    break
            days += 1
            poz += kroki
            poz += 1
