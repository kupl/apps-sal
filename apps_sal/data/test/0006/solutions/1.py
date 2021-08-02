T = int(input())
for _ in range(T):
    n, x = list(map(int, input().split()))
    damage = []
    maxi = []
    for i in range(n):
        d, h = list(map(int, input().split()))
        maxi.append(d)
        damage.append(d - h)
    damage.sort(reverse=True)
    maxi.sort(reverse=True)

    if damage[0] <= 0 and maxi[0] < x:
        print(-1)
    else:
        if maxi[0] >= x:
            print(1)
        else:
            print((x - maxi[0] - 1) // damage[0] + 2)
