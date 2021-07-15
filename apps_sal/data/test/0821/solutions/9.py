s, v1, v2, t1, t2 = map(int, input().split())
if t1 * 2 + v1 * s < t2 * 2 + v2 * s:
    print('First')
elif t1 * 2 + v1 * s == t2 * 2 + v2 * s:
    print('Friendship')
else:
    print('Second')
