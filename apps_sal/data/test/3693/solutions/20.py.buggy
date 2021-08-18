def check1(point):
    return sq1[0][0] <= point[0] <= sq1[3][0] and sq1[0][1] <= point[1] <= sq1[3][1]


def check2(point):
    return point[0] + sq2[0][1] - sq2[0][0] >= point[1] and point[0] + sq2[3][1] - sq2[3][0] <= point[1] and -point[0] + sq2[3][1] + sq2[3][0] >= point[1] and -point[0] + sq2[0][1] + sq2[0][0] <= point[1]


t = [int(i) for i in input().split()]
sq1 = list(zip(t[::2], t[1::2]))
sq1.sort()
t = [int(i) for i in input().split()]
sq2 = list(zip(t[::2], t[1::2]))
sq2.sort()
sq2[1], sq2[2] = sq2[2], sq2[1]
for i in range(-100, 101):
    for j in range(-100, 101):
        if check1((i, j)) and check2((i, j)):
            print("YES")
            return
print("NO")
