(A, B, C) = map(int, input().split())
if B + C <= A:
    print('0')
else:
    print(B + C - A)
