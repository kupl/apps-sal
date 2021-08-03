j, s, m = map(int, input().split())
m = m - j
if m >= (2 * s):
    m = m % (2 * s)
    if m >= s:
        print('Unlucky Chef')
    else:
        print('Lucky Chef')
elif(m >= s):
    print('Unlucky Chef')
else:
    print('Lucky Chef')
