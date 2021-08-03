n = int(input())
sticks = list(map(int, input().split()))

length = [0] * 1000000
miv = 1000000
mav = 0
answ = 0
for i in range(len(sticks)):
    length[sticks[i] - 1] = length[sticks[i] - 1] + 1
    if sticks[i] - 1 > mav:
        mav = sticks[i] - 1
    if sticks[i] - 1 < miv:
        miv = sticks[i] - 1

length = length[miv:mav + 1]
for i in range(len(length) - 1, -1, -1):
    if length[i] % 2 == 1:
        if i > 0 and length[i - 1] > 0:
            length[i] = length[i] - 1
            length[i - 1] = length[i - 1] + 1
        else:
            length[i] = length[i] - 1

square = []
for i in range(len(length) - 1, -1, -1):

    while length[i] > 0:
        square.append(i + miv + 1)
        length[i] = length[i] - 2
        if len(square) == 2:
            answ += square[0] * square[1]
            square = []
print(answ)
