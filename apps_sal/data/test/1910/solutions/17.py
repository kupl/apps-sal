
N = int(input())

sol = 0
i = 0

while i + N - 1 < (2 * N - 2):

    restL = i
    tmp = 1

    if restL >= 1:
        tmp *= 3
        restL -= 1

    if restL >= 0:
        tmp *= 4 ** restL

    restR = (2 * N - 2) - (i + N - 1) - 1

    if restR >= 1:
        tmp *= 3
        restR -= 1

    if restR >= 0:
        tmp *= 4 ** restR

    sol += tmp

    i += 1

print(4 * sol)
