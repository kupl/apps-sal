
n = int(input())
l = []


def cross(x1, y1, x2, y2):

    area = x1 * y2 - y1 * x2
    return area


for i in range(n):
    x, y = list(map(int, input().split()))
    l.append([x, y])
max_upper = 0
max_lower = 0
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        max_upper = 0
        max_lower = 0
        for k in range(n):
            if i != j and i != k and j != k:
                area = (l[j][0] - l[i][0]) * (l[k][1] - l[i][1]) - (l[j][1] - l[i][1]) * (l[k][0] - l[i][0])
                if area > 0:
                    if area > max_upper:
                        max_upper = area
                else:
                    if -area > max_lower and area != 0:
                        max_lower = -area

        if max_lower + max_upper > ans and max_lower != 0 and max_upper != 0:
            ans = max_lower + max_upper
print(ans / 2)
