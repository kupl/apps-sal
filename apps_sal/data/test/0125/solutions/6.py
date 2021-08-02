l = []
for i in range(4):
    l.append(list(map(int, input().split())))


def go():
    for i in range(4):
        if l[i][3] and (l[(i + 1) % 4][0] or l[(i + 3) % 4][2] or l[(i + 2) % 4][1] or l[i][0] or l[i][1] or l[i][2]):
            return False
    return True


if go():
    print("NO")
else:
    print("YES")
