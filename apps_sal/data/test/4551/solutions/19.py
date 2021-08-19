(A, B, C, D) = list(map(int, input().split()))
if 1 <= A and B and C and (D <= 10):
    if A + B == C + D:
        print('Balanced')
    elif A + B > C + D:
        print('Left')
    elif A + B < C + D:
        print('Right')
