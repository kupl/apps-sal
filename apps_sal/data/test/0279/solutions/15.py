v = input().split()
p = input().split()

v1 = int(v[0])

v2 = int(v[1])

T = int(p[0])
d = int(p[1])

x = abs(v1 - v2)
t = T - 2

sum = v1 + v2

if v1 <= v2:

    def check(v1, v2, d, t):
        a = []
        z = d
        for i in range(v1):

            if ((v1 + z) - v2) > (d * t + d):
                z -= 1

            else:
                a.append(z)

        return(int(a[0]))

    for i in range(t):

        if ((v1 + d) - v2) <= (d * (t - (i + 1)) + d):
            sum += (v1 + d)

            v1 = v1 + d
        else:
            sum += (v1 + check(v1, v2, d, t - (i + 1)))

else:
    v1, v2 = v2, v1

    def check(v1, v2, d, t):
        a = []
        z = d
        for i in range(v1):

            if ((v1 + z) - v2) > (d * t + d):
                z -= 1

            else:
                a.append(z)

        return(int(a[0]))

    for i in range(t):

        if ((v1 + d) - v2) <= (d * (t - (i + 1)) + d):
            sum += (v1 + d)

            v1 = v1 + d
        else:
            sum += (v1 + check(v1, v2, d, t - (i + 1)))


print(sum)
