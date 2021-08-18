def fun(c):
    return c[0]


def f(a, b, alice, bob, un, n, check):
    inf = 0
    if n - a <= a:
        inf = 0
        for i in range(n):
            inf += int(inp[i][1])
    else:

        tempb = 0
        j = 0
        for i in range(a):
            inf += alice[i][0]
            d[alice[i][1]] = 1
            if who[alice[i][1]][check] == "1":
                tempb += 1
            j += 1
        i = 0
        while(i < b and tempb < a):
            if d[bob[i][1]] == 0:
                inf += bob[i][0]
                tempb += 1
                j += 1
            i += 1
        if j < 2 * a:
            k = 0
            unn = len(un)
            while(j < 2 * a and i < b and k < unn):
                if (i < b and k < unn):
                    if (d[bob[i][1]] == 1):
                        i += 1
                    else:
                        if (bob[i][0] > un[k][0]):
                            inf += bob[i][0]
                            i += 1
                            j += 1
                        else:
                            inf += un[k][0]
                            k += 1
                            j += 1

            while(j < 2 * a and i < b):
                if (d[bob[i][1]] == 1):
                    i += 1
                else:
                    inf += bob[i][0]
                    i += 1
                    j += 1
            while(j < 2 * a and k < unn):
                inf += un[k][0]
                k += 1
                j += 1
    print(inf)


n = int(input())
d = {}
who = {}
inp = []
a = 0
b = 0
alice = []
bob = []
un = []
for i in range(n):
    t = input().split()
    if t[0][0] == "1":
        a += 1
        temp = [int(t[1]), i]
        d[i] = 0
        alice.append(temp)
    if t[0][1] == "1":
        b += 1
        temp = [int(t[1]), i]
        bob.append(temp)
        d[i] = 0
    if t[0][1] == t[0][0] and t[0][0] == "0":
        temp = [int(t[1]), i]
        un.append(temp)
    who[i] = t[0]
    inp.append(t)

alice.sort(key=fun, reverse=True)
bob.sort(key=fun, reverse=True)
un.sort(key=fun, reverse=True)
inf = 0

if a < b:
    f(a, b, alice, bob, un, n, 1)
else:
    f(b, a, bob, alice, un, n, 0)
