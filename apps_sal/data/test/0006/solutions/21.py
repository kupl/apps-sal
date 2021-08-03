T = int(input())

while T > 0:
    T -= 1
    n, head = map(int, input().split())

    possible = False
    eff = 0
    maxDmg = 0
    for i in range(n):
        kill, respawn = map(int, input().split())
        if kill > respawn:
            possible = True

        eff = max(eff, kill - respawn)
        maxDmg = max(maxDmg, kill)

    if maxDmg >= head:
        print(1)
    elif not possible:
        print(-1)
    else:
        print((head - maxDmg) // eff + (1 if (head - maxDmg) % eff else 0) + 1)
