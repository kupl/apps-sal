S = input()
m = int(S[5:7])
d = int(S[8:10])
if m < 4:
    print('Heisei')
elif m == 4:
    if d == 31:
        print('TBD')
    else:
        print('Heisei')
else:
    print('TBD')
