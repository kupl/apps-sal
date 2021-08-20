(a_1, a_2, a_3) = map(int, input().split())
sum = a_1 + a_2 + a_3
if sum > 21:
    print('bust')
else:
    print('win')
