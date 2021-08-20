(a, b) = map(int, input().split())
if a % 3 == 0 or b % 3 == 0 or a % 3 != b % 3:
    print('Possible')
else:
    print('Impossible')
