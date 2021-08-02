h, w = list(map(int, input().split()))
n = int(input())
a = [int(i) for i in input().split()]

color = [[None] * w for _ in range(h)]


def zigzag(h, w):
    ih, iw = 0, 0

    while ih < h:
        yield (ih, iw)

        if ih % 2 == 0:
            if iw == w - 1:
                ih += 1
            else:
                iw += 1
        else:
            if iw == 0:
                ih += 1
            else:
                iw -= 1


ia = 0
ic = 0

for ih, iw in zigzag(h, w):
    ia += 1
    if ia > a[ic]:
        ic += 1
        ia = 1

    color[ih][iw] = ic + 1


for row in color:
    print((' '.join(map(str, row))))
