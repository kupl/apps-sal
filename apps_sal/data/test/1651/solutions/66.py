(S, P) = map(int, input().split())
if S == 0 and P == 0:
    print('Yes')
else:
    N = (-S + pow(S ** 2 - 4 * P, 0.5)) / 2
    M = (-S - pow(S ** 2 - 4 * P, 0.5)) / 2
    if int(N) == 0 or int(M) == 0:
        print('No')
    elif N.is_integer() == False or M.is_integer() == False:
        print('No')
    else:
        print('Yes')
