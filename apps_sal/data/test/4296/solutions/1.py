lst = list(map(int, input().split()))
if sum(lst) <= 21:
    print('win')
else:
    print('bust')
