#E70_B

st = list(input())

counts = []

for i in range(0, 10):
    counts.append(0)

for i in range(1, len(st)):
    counts[(int(st[i]) - int(st[i - 1]) + 10) % 10] += 1

for x in range(0, 10):
    st = ""
    for y in range(0, 10):
        s = 0
        f = False
        for i in range(0, 10):
            if counts[i] == 0:
                continue
            j = 0
            c = 100000000000
            ff = False
            f = False
            while j < 10:
                k = 0
                while k < 10:
                    if j == 0 and k == 0:
                        k += 1
                        continue
                    if ((x * j) + (y * k)) % 10 == i:
                        c = min(c, j + k)
                        ff = True
                    k += 1
                j += 1

            if ff:
                s += counts[i] * (max(1, c) - 1)
                f = True
            if not f:
                s = -1
                break
        st += str(s)
        if y != 9:
            st += " "
    print(st)

