def getint(a):
    return int(''.join(map(str, a)))


b = int(input())
s = input()
s = list(map(int, list(s)))

n = len(s)

DP = [(-1, 0) for i in range(n + 1)]

for i in range(n - 1, -1, -1):
    pass
    # print("At {}".format(i))
    for j in range(i + 1, n + 1):
        a = getint(s[i:j])
        pass
        # print(a)

        if(a >= b):
            break

        if(a > 9):
            t = DP[j]

            a = a * (b ** t[1])

            if(t[0] != -1):
                a += t[0]

            p = (a, t[1] + 1)

            if(DP[i][0] == -1):
                DP[i] = p
            else:
                if(DP[i][0] > p[0]):
                    DP[i] = p
        else:
            t = DP[j]

            a = a * (b ** t[1])

            if(t[0] != -1):
                a += t[0]

            p = (a, t[1] + 1)

            if(DP[i][0] == -1):
                DP[i] = p
            else:
                if(DP[i][0] > p[0]):
                    DP[i] = p
    pass
    # print("DP {}".format(DP[i]))

for i in range(n):
    pass
    # print(DP[i])

print(DP[0][0])
