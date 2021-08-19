t = int(input())
while t > 0:
    t -= 1
    (s, i, e) = [int(x) for x in input().split()]
    ms = s + e
    if ms <= i:
        print(0)
    else:
        c = (ms - i + 1) // 2
        print(min(c, e + 1))
