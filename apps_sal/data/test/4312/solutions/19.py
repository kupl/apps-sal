A, B, C, D = map(int, input().split())
while A > 0 and C > 0:
    C = C - B
    if C <= 0:
        print('Yes')
        break
    else:
        A = A - D
        if A <= 0:
            print('No')
            break
