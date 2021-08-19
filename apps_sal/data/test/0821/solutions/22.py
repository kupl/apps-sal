(s, v1, v2, t1, t2) = map(int, input().split())
if v1 * s + t1 * 2 < v2 * s + t2 * 2:
    print('First')
elif v1 * s + t1 * 2 > v2 * s + t2 * 2:
    print('Second')
else:
    print('Friendship')
