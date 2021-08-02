c = []
for i in range(3):
    c.append([int(x) for x in input().split()])
res = "No"
for i in range(101):
    for j in range(101):
        for k in range(101):
            if c[0][0] - i == c[1][0] - j == c[2][0] - k:
                if c[0][1] - i == c[1][1] - j == c[2][1] - k:
                    if c[0][2] - i == c[1][2] - j == c[2][2] - k:
                        res = "Yes"
print(res)
