c = [list(map(int, input().split())) for _ in range(3)]

if sum([sum(i) for i in c]) % 3 != 0:
    print("No")
else:
    a0 = 0
    b0, b1, b2 = c[0][0], c[0][1], c[0][2]
    a1, a2 = c[1][0] - b0, c[2][0] - b0
    if c[1][1] == a1 + b1 and c[1][2] == a1 + b2 and c[2][1] == a2 + b1 and c[2][2] == a2 + b2:
        print("Yes")
    else:
        print("No")

