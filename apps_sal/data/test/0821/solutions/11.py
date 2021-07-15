s, v1, v2, t1, t2 = [int(i) for i in input().split()]
tm1 = s * v1 + 2 * t1
tm2 = s * v2 + 2 * t2
if tm1 == tm2:
    print('Friendship')
elif tm1 > tm2:
    print('Second')
else:
    print('First')
