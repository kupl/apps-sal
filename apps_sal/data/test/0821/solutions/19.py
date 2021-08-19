(s, v1, v2, t1, t2) = map(int, input().split())
if v1 * s + 2 * t1 == v2 * s + 2 * t2:
    print('Friendship')
if v1 * s + 2 * t1 < v2 * s + 2 * t2:
    print('First')
if v1 * s + 2 * t1 > v2 * s + 2 * t2:
    print('Second')
