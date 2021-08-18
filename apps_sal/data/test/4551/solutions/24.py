A, B, C, D = list(map(int, input().split()))
if (1 <= A and A <= 10) and (1 <= B and B <= 10) and (1 <= C and C <= 10) and (1 <= D and D <= 10):
    L = A + B
    R = C + D
    if L > R:
        print('Left')
    elif L == R:
        print('Balanced')
    elif L < R:
        print('Right')
