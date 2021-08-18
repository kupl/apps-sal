t = int(input())

for case in range(t):
    n = int(input())
    s = input()

    groups = [s[0]]
    for x in s[1:]:
        if x == groups[-1][-1]:
            groups[-1] += x
        else:
            groups.append(x)

    groups = [len(x) for x in groups]
    to_use = 0

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

        groups[to_use] -= 1
        groups[i] = 0
        ops += 1
    else:
        print(ops)
        continue

    size = len(groups) - i
    ops += (size + 1) // 2
    print(ops)
