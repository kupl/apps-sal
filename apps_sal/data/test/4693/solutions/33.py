A, B = map(int, input().split())
if 1 <= A and B <= 9:
    if A + B >= 10:
        print('error')
    else:
        print(A + B)
