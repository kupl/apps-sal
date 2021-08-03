S = input()
if S.count('R') == 2:
    if S == 'RSR':
        print(1)
    else:
        print(2)
else:
    print(S.count('R'))
