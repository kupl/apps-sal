
def check(gears):
    for i in range(0, len(gears)):
        if gears[i] != i:
            return False
    return True


# print((0-1)%3)
n = int(input())
gears = [int(i) for i in input().split()]
saved = set()
while True:
    current = str(gears)
    if current in saved:
        break
    saved.add(current)
    for i in range(0, n):
        if i % 2 == 0:
            gears[i] = (gears[i] + 1) % n
        else:
            gears[i] = (gears[i] - 1) % n
    if check(gears):
        break
    # print("HI")
if check(gears):
    print("Yes")
else:
    print("No")
