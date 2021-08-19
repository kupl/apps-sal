d = [list(map(int, input().split())) for i in range(int(input()))]

s = 0

for k in range(1, 10001):

    p = [min(max((k - l) / (r - l + 1), 1e-20), 1) for l, r in d]

    u = v = 1

    for r in p:
        u *= r

    for r in p:

        v *= r

        s += (u - v) * (r - 1) / r

print(s)


# Made By Mostafa_Khaled
