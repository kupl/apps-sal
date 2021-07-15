import sys
s, v1, v2, t1, t2 = list(map(int, input().split()))
tt1 = v1 * s + 2 * t1
tt2 = v2 * s + 2 * t2
if (tt1 < tt2):
    print('First')
elif tt1 == tt2:
    print('Friendship')
else:
    print('Second')

