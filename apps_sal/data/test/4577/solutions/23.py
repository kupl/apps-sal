# 061_a
A, B, C = list(map(int, input().split()))
if (-100 <= A <= 100) and (-100 <= B <= 100) and (-100 <= C <= 100):
    if A <= C and C <= B:
        print('Yes')
    else:
        print('No')
