(n, k) = list(map(int, input().split()))
l = [int(x) for x in input().split()]
maps = []
for _ in range(256):
    maps.append(['empty', 0])
output = []
for innum in l:
    if maps[innum][0] == 'chosen':
        outnum = maps[innum][1]
    elif maps[innum][0] == 'potential':
        outnum = maps[innum][1]
        i = innum
        while i >= 0 and maps[i][0] == 'potential':
            maps[i] = ['chosen', outnum]
            i -= 1
    else:
        i = innum
        while i >= 0 and i >= innum - (k - 1) and (maps[i][0] != 'chosen'):
            i -= 1
        i += 1
        outnum = i
        for j in range(outnum, innum + 1):
            maps[j] = ['chosen', outnum]
        if innum < 255:
            for j in range(innum + 1, min(256, outnum + k)):
                if maps[j][0] != 'chosen':
                    maps[j] = ['potential', outnum]
    output.append(str(outnum))
print(' '.join(output))
