(a, b) = input().split()
if int(a) % 3 == 0 or int(b) % 3 == 0 or (int(a) + int(b)) % 3 == 0:
    print('Possible')
else:
    print('Impossible')
