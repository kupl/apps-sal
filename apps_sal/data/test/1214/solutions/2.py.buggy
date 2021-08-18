import sys
import math

n = int(input())
A = list(map(int, input().split()))


ANS = [None] * (n // 2 + 1)
ANS[0] = [0, 0]

for i in range(n // 2):
    NEXT = []

    # x**2=?
    # y**2=A[i//2]

    z = A[i]

    xr = math.ceil(math.sqrt(z))

    LIST = []
    for j in range(1, xr + 1):
        if z % j == 0:
            LIST.append(j)
    # print(LIST)

    for l in LIST[::-1]:
        if (l + z // l) % 2 == 1:
            continue
        y = (l + z // l) // 2
        x = y - l
        # print(x,y)

        _, N = ANS[i]
        if x**2 > N:
            NEXT = [x**2, y**2]
            break

    # print(NEXT)
    if NEXT == []:
        print("No")
        return

    ANS[i + 1] = NEXT


# print(ANS)

print("Yes")
for i in range(1, n // 2 + 1):
    print(ANS[i][0] - ANS[i - 1][1], end=" ")
    print(ANS[i][1] - ANS[i][0], end=" ")
