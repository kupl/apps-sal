n = int(input())
brick = list(map(int, input().split()))

if 1 not in brick:
    print((-1))
else:
    a = 1
    for x in brick:
        if x == a:
            a += 1
    print((n - a + 1))
