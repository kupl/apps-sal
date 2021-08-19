H, n = list(map(int, input().split()))
ds = [int(x) for x in input().split()]

h = H
mn = 0
for i, d in enumerate(ds):
    h += d
    mn = min(mn, h - H)
    if h <= 0:
        print(i + 1)
        break
else:
    sd = sum(ds)
    if sd >= 0:
        print(-1)
    else:
        sd = -sd
        # print(mn, sd)
        repeat = (H + mn) // sd
        h = H - repeat * sd
        # print(repeat, h)
        for i, d in enumerate(ds):
            h += d
            if h <= 0:
                print(repeat * n + i + 1)
                break
        else:
            for i, d in enumerate(ds):
                h += d
                if h <= 0:
                    print(repeat * n + i + 1 + n)
                    break
