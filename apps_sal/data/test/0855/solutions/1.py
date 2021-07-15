def readln(): return list(map(int, input().rstrip().split()))


def score_of(x, y):
    if x == y:
        return 0, 0
    elif x == 3 and y == 2:
        return 1, 0
    elif x == 2 and y == 3:
        return 0, 1
    elif x == 2 and y == 1:
        return 1, 0
    elif x == 1 and y == 2:
        return 0, 1
    elif x == 1 and y == 3:
        return 1, 0
    elif x == 3 and y == 1:
        return 0, 1


k, a, b = readln()
A, B = [[0 for i in range(4)] for j in range(4)], [[0 for i in range(4)] for j in range(4)]
for i in range(1, 4):
    a1, a2, a3 = readln()
    A[i][1], A[i][2], A[i][3] = a1, a2, a3
for i in range(1, 4):
    a1, a2, a3 = readln()
    B[i][1], B[i][2], B[i][3] = a1, a2, a3

circle = set()
circle_score = [(0, 0)]
circle_data = []
x, y = a, b
while (x, y) not in circle and k > 0:
    circle.add((x, y))
    circle_data.append((x, y))
    x_, y_ = score_of(x, y)
    circle_score.append((circle_score[-1][0] + x_, circle_score[-1][1] + y_))
    x, y = A[x][y], B[x][y]
    k -= 1

if k == 0:
    print("{} {}".format(circle_score[-1][0], circle_score[-1][1]))
    return

pre_idx = circle_data.index((x, y))
freq = len(circle_data) - pre_idx
fscorea, fscoreb = circle_score[-1][0] - circle_score[pre_idx][0], circle_score[-1][1] - circle_score[pre_idx][1]
p = k // freq
rsa = circle_score[-1][0] + fscorea * p
rsb = circle_score[-1][1] + fscoreb * p
r = k % freq

while r > 0:
    x_, y_ = score_of(x, y)
    rsa += x_
    rsb += y_
    x, y = A[x][y], B[x][y]
    r -= 1
print("{} {}".format(rsa, rsb))

