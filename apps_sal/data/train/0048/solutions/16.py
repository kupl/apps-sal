t = int(input())
for ii in range(t):
    (x, y, k) = map(int, input().split())
    coals = k
    sticks = k
    sticks = k * y + k
    num = (sticks - 1) // (x - 1)
    if (sticks - 1) % (x - 1) != 0:
        num += 1
    num += k
    print(num)
