n = int(input())
xy = [[int(item) for item in input().split()] for _ in range(n)]

# If mod2 changes, there are no answer
mod2 = (xy[0][0] + xy[0][1]) % 2
for x, y in xy:
    if (x + y) % 2 != mod2:
        print(-1)
        return

if mod2 == 1:
    print(31)
    print(" ".join([str(2**item) for item in range(31)]))
else:
    print(32)
    print("1 " + " ".join([str(2**item) for item in range(31)]))

for x, y in xy:
    if mod2 == 0:
        x -= 1
        print("R", end="")
    u = x + y
    v = x - y
    bits = [[0] * 31 for _ in range(2)]
    if u < 0:
        bits[0] = [1] * 31
        bits[0][30] = 0
    else:
        bits[0][30] = 1
    if v < 0:
        bits[1] = [1] * 31
        bits[1][30] = 0
    else:
        bits[1][30] = 1
    for i in range(30):
        if u >= 0 and abs(u)//2>>i & 1:
            bits[0][i] = 1
        if u < 0 and abs(u)//2>>i & 1:
            bits[0][i] = 0
        if v >= 0 and abs(v)//2>>i & 1:
            bits[1][i] = 1
        if v < 0 and abs(v)//2>>i & 1:
            bits[1][i] = 0
    for u_b, v_b in zip(bits[0], bits[1]):
        if u_b == 1 and v_b == 1:
            print("R", end="")
        elif u_b == 0 and v_b == 0:
            print("L", end="")
        elif u_b == 1 and v_b == 0:
            print("U", end="")
        elif u_b == 0 and v_b == 1:
            print("D", end="")
    print("")

