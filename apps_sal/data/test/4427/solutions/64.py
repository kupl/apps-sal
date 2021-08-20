[r, D, x] = [int(_) for _ in input().split()]
for i in [0] * 10:
    print((x := (r * x - D)))
