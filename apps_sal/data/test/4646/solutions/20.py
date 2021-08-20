def mi():
    return map(int, input().split())


'\n4\n4\n3 2 7 6\n3\n3 2 6\n1\n7\n7\n4 9 2 1 18 3 0\n'
for _ in range(int(input())):
    n = int(input())
    a = list(mi())
    (o, e) = (0, 0)
    for i in range(n):
        if i % 2:
            if a[i] % 2 == 0:
                o += 1
        elif a[i] % 2:
            e += 1
    if o == e:
        print(o)
    else:
        print(-1)
