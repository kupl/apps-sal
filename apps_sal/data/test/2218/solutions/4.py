n, k = list(map(int, input().split()))
soldiers = list(map(int, input().split()))
count = 0
seen = {0: 0}
while count != k:
    for beauty, bits in list(seen.items()):
        for i, x in enumerate(soldiers):
            if (bits & (1 << i)) != 0 or beauty + x in seen:
                continue
            new_bits = (bits | (1 << i))
            seen[beauty + x] = new_bits
            #print('%d + %d = %d' % (beauty, x, beauty+x))
            group = []
            for j, y in enumerate(soldiers):
                if (new_bits & (1 << j)) != 0:
                    group.append(y)
            print(' '.join(map(str, [len(group)] + group)))
            count += 1
            if count == k:
                break
        if count == k:
            break
