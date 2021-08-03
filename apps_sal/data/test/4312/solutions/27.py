A, B, C, D = list(map(int, input().split()))

turn = 0
while A > 0 and C > 0:
    if turn == 0:
        C -= B
        turn = 1
    else:
        A -= D
        turn = 0

if A <= 0:
    print('No')
else:
    print('Yes')
