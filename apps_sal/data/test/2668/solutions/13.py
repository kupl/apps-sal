(j, s, m) = map(int, input().split())
rem = m - j
n = rem // s
if n % 2 == 0:
    print('Lucky Chef')
else:
    print('Unlucky Chef')
