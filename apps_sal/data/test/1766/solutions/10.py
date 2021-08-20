n = int(input())
z = [int(x) for x in input().split()]
tot1 = 0
tot2 = 0
if len(z) % 2 == 0:
    while len(z) > 0:
        tot1 += max(z[0], z[-1])
        z.remove(max(z[0], z[-1]))
        tot2 += max(z[0], z[-1])
        z.remove(max(z[0], z[-1]))
    print(str(tot1) + ' ' + str(tot2))
else:
    while 1:
        tot1 += max(z[0], z[-1])
        z.remove(max(z[0], z[-1]))
        if len(z) == 0:
            break
        else:
            tot2 += max(z[0], z[-1])
            z.remove(max(z[0], z[-1]))
            if len(z) == 0:
                break
            else:
                continue
    print(str(tot1) + ' ' + str(tot2))
