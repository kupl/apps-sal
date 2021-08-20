(s, v1, v2, t1, t2) = list(map(int, input().split()))
if t1 + s * v1 + t1 < t2 + s * v2 + t2:
    print('First')
elif t1 + s * v1 + t1 > t2 + s * v2 + t2:
    print('Second')
else:
    print('Friendship')
