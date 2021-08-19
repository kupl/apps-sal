(A, B) = map(int, input().split())
if (1 <= A and A <= 100) and (1 <= B and B <= 100):
    sum = A + B
    if A % 3 == 0 or B % 3 == 0 or sum % 3 == 0:
        print('Possible')
    else:
        print('Impossible')
