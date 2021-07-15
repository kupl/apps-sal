a, b, c = map(int, input().split())

can_listen = b // a

if can_listen < c:
    print(can_listen)
else:
    print(c)
