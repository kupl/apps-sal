n = int(input())
location = list(map(str, [input() for i in range(n)]))
fail = 0
for j in range(n):
    if j == 0:
        a = [0, 0, 0]
    else:
        a = list(map(int, location[j - 1].split()))
    b = list(map(int, location[j].split()))
    x = abs(a[1] - b[1])
    y = abs(a[2] - b[2])
    t = b[0] - a[0]
    if x + y <= t:
        if (x + y) % 2 == t % 2:
            pass
        else:
            fail += 1
    else:
        fail += 1
if fail == 0:
    print("Yes")
else:
    print("No")
