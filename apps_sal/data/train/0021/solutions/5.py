t = int(input())

for k in range(t):
    n = int(input())
    a = set(map(int, input().split()))
    for x in range(1, 1025):
        if set(x ^ q for q in a) == a:
            print(x)
            break
    else:
        print(-1)
