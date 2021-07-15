for _ in range(int(input())):
    s = input()
    se = set()
    total = 0
    curr = [0, 0]
    for e in s:
        seg = ()
        if e == "E":
            seg = (curr[0], curr[1], 0)
            curr[0] += 1
        elif e == "N":
            seg = (curr[0], curr[1], 1)
            curr[1] += 1
        elif e == "W":
            seg = (curr[0]-1, curr[1], 0)
            curr[0] -= 1
        elif e == "S":
            seg = (curr[0], curr[1]-1, 1)
            curr[1] -= 1
        
        if seg in se:
            total += 1
        else:
            total += 5
            se.add(seg)
    print(total)
