s, v1, v2, t1, t2 = map(int, input().split())

a1 = v1 * s + 2 * t1
a2 = v2 * s + 2 * t2

if a1 < a2:
    print('First')
elif a2 < a1:
    print('Second')
else:
    print('Friendship')
