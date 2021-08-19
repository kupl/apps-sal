(a, b, c, d, e) = list(map(int, input().split()))
ans1 = a * b + 2 * d
ans2 = a * c + 2 * e
if ans1 == ans2:
    print('Friendship')
elif ans1 > ans2:
    print('Second')
else:
    print('First')
