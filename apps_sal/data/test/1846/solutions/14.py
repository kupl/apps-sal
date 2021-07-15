with open("input.txt", "r") as f:
    n = int(f.readline())
    t = list(map(int, f.readline().split()))

m = 0
for i in range(1, n):
    if t[i] <= 0:
        m += 1

if t[0] >= 0:
    m += 1


p = m
for i in range(1, n - 1):
    if t[i] < 0:
        cost = -1
    elif t[i] == 0:
        cost = 0
    else:
        cost = 1

    p += cost
    m = min(m, p)


with open("output.txt", "w") as f:
    f.write(str(m))

