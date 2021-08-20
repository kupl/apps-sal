for _ in range(int(input())):
    x = int(input())
    r = [int(x) for x in input().split()]
    is_s = False
    last_z = 0
    tot = 0
    for i in r:
        if i == 1:
            if not is_s:
                is_s = True
                last_z = 0
            else:
                last_z = 0
        elif is_s:
            last_z += 1
            tot += 1
    print(tot - last_z)
