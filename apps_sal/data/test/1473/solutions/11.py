n = int(input())
queue = []
dist = [0] * 1000001
dist2 = [0] * 1000001
dictx = {}
dictx2 = {}
for i in range(n):
    a, b = map(int, input().split(' '))
    dictx[a] = b
    dictx2[b] = a
    dist[a] += 1
    dist[b] += 1
    dist2.append(a)
    dist2.append(b)
if n % 2 == 0:
    indx = 0
    final = [0] * n
    curr = 0
    while curr in dictx:
        curr = dictx[curr]
        final[2 * indx + 1] = str(curr)
        indx += 1

    indx = -1
    curr = 0
    while curr in dictx2:
        curr = dictx2[curr]
        final[2 * indx] = str(curr)
        indx -= 1

    print(' '.join(final))

if n % 2 == 1:
    yes = False
    maf = []
    for i in dist2:
        if dist[i] == 1:
            maf.append(i)

    if maf[0] in dictx.keys():
        frontmaf = maf[0]
    else:
        frontmaf = maf[1]

    indx = 0
    final = [0] * n
    curr = frontmaf
    while curr in dictx:
        final[2 * indx] = str(curr)
        curr = dictx[curr]
        indx += 1
    final[2 * indx] = str(curr)

    indx = 0
    curr = 0
    while curr in dictx and dictx[curr] != 0:
        curr = dictx[curr]
        final[2 * indx + 1] = str(curr)
        indx += 1

    print(' '.join(final))
