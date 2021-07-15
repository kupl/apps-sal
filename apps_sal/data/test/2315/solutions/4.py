t = int(input())
for i in range(t):
    l, r = list(map(int,input().split()))
    if 2 * l <= r:
        print(l, 2 * l)

