T = int(input())
p = []
i = 0
np = 0
while np < 10 ** 9:
    i += 1
    np += 3 * i - 1
    p.append(np)
for case in range(T):
    t = int(input())
    c = 0
    while t >= 2:
        for e in p[::-1]:
            if t >= e:
                t -= e
                c += 1
                break
    print(c)
