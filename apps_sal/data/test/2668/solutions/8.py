(jc, sc, m) = (int(i) for i in input().split())
if (m - jc) // sc % 2 == 0:
    print('Lucky Chef')
else:
    print('Unlucky Chef')
