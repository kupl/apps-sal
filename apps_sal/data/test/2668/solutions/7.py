(j, s, m) = map(int, input().split())
m = (m - j) // s
if m % 2 == 0:
    print('Lucky Chef')
else:
    print('Unlucky Chef')
