(a, b, c) = list(map(int, input().split()))
can_listen = b // a
if can_listen >= c:
    print(c)
else:
    print(can_listen)
