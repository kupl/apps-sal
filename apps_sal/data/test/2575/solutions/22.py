for i in range(int(input())):
    j = 360.0 / (180 - int(input()))
    print('YNEOS'[bool(j - int(j))::2])
