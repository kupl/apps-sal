_, m, d = map(int, input().split('/'))

if m < 4:
    print('Heisei')
else:
    if m == 4 and d < 31:
        print('Heisei')
    else:
        print("TBD")
