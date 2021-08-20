import sys
input1 = sys.stdin.readline


def solve():
    (n, s) = [int(i) for i in input1().split()]
    empl = []
    for i in range(n):
        empl.append([int(j) for j in input1().split()])
    empl.sort(reverse=True)
    lg = 0
    rg = 10 ** 9 + 1
    while rg - lg > 1:
        mg = (rg + lg) // 2
        need = (n + 1) // 2
        money = s
        for i in range(n):
            li = empl[i][0]
            ri = empl[i][1]
            if ri >= mg and need > 0:
                money -= max(mg, li)
                need -= 1
            else:
                money -= li
        if need == 0 and money >= 0:
            check = True
        else:
            check = False
        if check:
            lg = mg
        else:
            rg = mg
    print(lg)


t = int(input1())
while t > 0:
    empl = []
    solve()
    t -= 1
