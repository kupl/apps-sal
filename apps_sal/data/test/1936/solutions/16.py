t = int(input())

for _ in range(t):
    #n = int(input())
    l, r = list(map(int, input().split()))
    #l = list(map(int, input().split()))

    if 2 * l <= r:
        print(l, 2 * l)
    else:
        print(-1, -1)
