t = int(input())
for _ in range(t):
    n = int(input())
    bacteria = 1
    tw = 1
    res = []
    while tw < n:
        rem = n - tw
        if bacteria > rem:
            print(1 / 0)
            break
        if rem - bacteria <= bacteria:
            new = rem - bacteria
        else:
            new = max(0, min(bacteria, rem - 3 * bacteria))
        res.append(new)
        bacteria += new
        tw += bacteria
    print(len(res))
    print(*res)
