packs = list(map(int, input().split()))

if packs[0] + packs[1] == packs[2] or packs[0] + packs[2] == packs[1] or packs[2] + packs[1] == packs[0]:
    print('Yes')
else:
    print('No')
