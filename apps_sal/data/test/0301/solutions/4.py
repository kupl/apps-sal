(u, v) = list(map(int, input().split()))
if u > v or (v - u) % 2:
    print('-1')
elif u == v == 0:
    print('0\n')
elif u == v:
    print('1\n%d' % u)
else:
    diff = (v - u) // 2
    if diff & u == 0:
        print('2\n%d %d' % (u | diff, diff))
    else:
        print('3\n%d %d %d' % (diff, diff, u))
