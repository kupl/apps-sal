from sys import stdin
input = stdin.readline
q = int(input())
for _ in range(q):
    h, c, t = map(int, input().split())
    if 2 * t <= h + c:
        print(2)
    else:
        t *= 2
        h *= 2
        c *= 2
        w = h // 2 - c // 2
        pod = (h + c) // 2
        goal = t - pod
        if goal == 0:
            print(1)
        else:
            x = w // goal
            wynik = 2
            mini = 23649823847238
            for szkl in range(x - 3, x + 4):
                if szkl % 2 == 1 and szkl >= 1 and abs(goal - w / szkl) < mini:
                    mini = abs(goal - w / szkl)
                    wynik = szkl
            print(wynik)
