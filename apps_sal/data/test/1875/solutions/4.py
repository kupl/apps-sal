n = int(input())
a = []
area = 0
for i in range(n):
    a.append([int(i) for i in input().split(' ')])


def get_s(p1, p2, p3):
    return ((p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])) / 2.0


for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        positive = 0
        negative = 0
        for k in range(len(a)):
            if k == i or k == j:
                continue
            s = get_s(a[i], a[j], a[k])
            if s > 0:
                positive = max(positive, s)
            if s == 0:
                pass
            else:
                negative = min(negative, s)
        if positive != 0 and negative != 0:
            area = max(area, positive - negative)

print(area)

