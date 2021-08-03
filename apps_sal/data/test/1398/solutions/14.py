f = open("input.txt", "r")
f1 = open("output.txt", "w")


def search(mas, val):
    p = 0
    ost = len(mas) - 1
    while (p <= ost):
        mid = (p + ost) // 2
        if mas[mid] > val * 2:
            ost = mid - 1
        else:
            p = mid + 1

    return p


n = int(f.readline())
ma = n - 1
l = list(map(int, f.readline().split()))
l = sorted(l)

for i in range(n):
    e = search(l, l[i])

    w = i + n - e
    ma = min(ma, w)
ma = str(ma)
f1.write(ma)
f.close()
f1.close()
