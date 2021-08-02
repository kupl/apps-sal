n = int(input())
ls = [list(map(int, input().split())) for _ in range(n - 1)]


def culc(nt, p):
    if nt == 0:
        if p != n - 1:
            nt = ls[p][1] + ls[p][0]
            culc(nt, p + 1)
        else:
            print((0))
    else:
        if p != n - 1:
            if nt >= ls[p][1]:
                m = (nt - ls[p][1]) // ls[p][2]
                if (nt - ls[p][1]) % ls[p][2] != 0:
                    m += 1
                nt = ls[p][1] + ls[p][2] * m + ls[p][0]
                culc(nt, p + 1)
            else:
                nt = ls[p][1] + ls[p][0]
                culc(nt, p + 1)
        else:
            print(nt)


for i in range(n):
    culc(0, i)
