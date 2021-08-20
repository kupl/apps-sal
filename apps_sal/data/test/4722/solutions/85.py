(A, B) = map(int, input().split())
Total = A + B
if A % 3 == 0 or B % 3 == 0 or Total % 3 == 0:
    print('Possible')
else:
    print('Impossible')
