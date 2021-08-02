j, s, m = map(int, input().split())
m -= j
x = m // s
if(x % 2 == 0):
    print('Lucky Chef')
else:
    print('Unlucky Chef')
