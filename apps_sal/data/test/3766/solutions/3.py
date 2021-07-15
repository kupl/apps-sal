input()
colour = dict(list(zip('RGBYW', list(range(5)))))
cards = {(colour[c], ord(v) - ord('1')) for c, v in input().split()}

print((min(bin(cs).count('1') + bin(vs).count('1')
    for cs in range(1<<5) for vs in range(1<<5)
    if len({
        (c if (cs >> c) & 1 else -1, v if (vs >> v) & 1 else -1)
        for c, v in cards
    }) == len(cards)
)))

