(A, B) = list(map(int, input().split()))
C = A + B
if (A >= 3) & (A % 3 == 0) | (B >= 3) & (B % 3 == 0) | (C >= 3) & (C % 3 == 0):
    print('Possible')
else:
    print('Impossible')
