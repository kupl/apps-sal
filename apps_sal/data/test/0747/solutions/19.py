

n, x = (int(x) for x in input().split())



cs = []

for i in range(n):

    cs.append([int(x) for x in input().split()])

    if cs[-1][0] > 0:

        cs[-1][0] = 1



def try_eat(t0):

    h0 = x

    used = set()

    while True:

        m0 = 0

        i0 = -1

        for i, (t, h, m) in enumerate(cs):

            if t != t0 and h <= h0 and m > m0 and i not in used:

                m0 = m

                i0 = i

        if i0 == -1:

            break



        used.add(i0)

        h0 += cs[i0][2]

        t0 = 1 - t0



    return len(used)



print(max(try_eat(0), try_eat(1)))



# Made By Mostafa_Khaled

