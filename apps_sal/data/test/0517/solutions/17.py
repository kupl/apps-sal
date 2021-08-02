n, d, h = list(map(int, input().split()))
if d == h == 1 and n == 2 or (d == h != 1 or d != h) and 2 * h >= d:
    node = 1
    while node < d + 1:
        if node == h + 1:
            print("{0} {1}".format(1, node + 1))
        else:
            print("{0} {1}".format(node, node + 1))
        node += 1
    node += 1
    node1 = 2 if d == h else 1
    while node <= n:
        print("{0} {1}".format(node1, node))
        node += 1
else:
    print(-1)
