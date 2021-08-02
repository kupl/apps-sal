import math
n = int(input())

ab = [None] * n
for i in range(n):
    ab[i] = tuple(map(int, input().split()))


def div(n):
    LIST = []
    while n != 1:
        check = 0
        for i in range(2, 1 + math.ceil(math.sqrt(n))):
            if n % i == 0:
                LIST.append(i)
                n = n // i
                check = 1
                break

        if check == 0:
            LIST.append(n)
            break

    return LIST


ANS = list(set(div(ab[0][0]) + div(ab[0][1])))

# print(ANS)

for i in range(1, n):
    ANSX = []
    for j in ANS:
        if ab[i][0] % j == 0 or ab[i][1] % j == 0:
            ANSX.append(j)

    ANS = ANSX

if ANS == []:
    print(-1)
else:
    print(ANS[0])
