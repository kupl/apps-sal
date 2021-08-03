X, Y = list(map(int, input().split()))

flag = True
for kame in range(X + 1):
    tsuru = X - kame
    if (4 * kame + 2 * tsuru == Y):
        print('Yes')
        flag = False
        break

if(flag):
    print('No')
