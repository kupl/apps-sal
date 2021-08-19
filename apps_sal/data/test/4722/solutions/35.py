(A_mai, B_mai) = map(int, input().split())
summ = A_mai + B_mai
if A_mai % 3 == 0 or B_mai % 3 == 0 or summ % 3 == 0:
    print('Possible')
else:
    print('Impossible')
