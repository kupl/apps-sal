''' Nastya and Rice
'''


''' routine '''

T = int(input())

for test in range(T):
    N, A, B, C, D = list(map(int, input().split()))

    lowerbound, upperbound = N * (A - B), N * (A + B)
    if lowerbound > (C + D) or upperbound < (C - D):
        print('No')
    else:
        print('Yes')
