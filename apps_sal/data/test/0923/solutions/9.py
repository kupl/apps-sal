n = int(input())
gears = list(map(int, input().split()))
blah = sorted([i for i in range(n)])
good = False
for push in range(n):
    for i in range(len(gears)):
        if i % 2 == 0:
            gears[i] += 1
            if gears[i] == n:
                gears[i] = 0
        else:
            gears[i] -= 1
            if gears[i] == -1:
                gears[i] = n-1
    if gears == blah:
        print("Yes")
        good = True
        break
if not good:
    print("No")

