t = int(input())

for case in range(t):
    n = int(input())
    s = input()
    #print("Input read in OK", n, s)

    groups = [s[0]]
    for x in s[1:]:
        if x == groups[-1][-1]:
            groups[-1] += x
        else:
            groups.append(x)

    groups = [len(x) for x in groups]
    to_use = 0
    #print("groups are", groups)

    ops = 0
    for i, x in enumerate(groups):
        while to_use < len(groups):
            if to_use < i:
                to_use += 1
                continue
            if groups[to_use] <= 1:
                to_use += 1
                continue
            break
        else:
            break

        #print("using", to_use)
        groups[to_use] -= 1
        groups[i] = 0
        ops += 1
    else:
        print(ops)
        continue

    # We now have a situation where the grid is of the form 10101010.
    # What do we do? Well,
    # 1010 (even length = n/2)
    # 10101 (odd length = (n + 1)/2)
    # so (n+1)/2 it is
    #print("ops before was", ops)
    size = len(groups) - i
    #print("size is", size)
    ops += (size + 1) // 2
    print(ops)
        
        

