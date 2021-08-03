n = int(input())
s = [int(x) for x in input()]
m = [int(x) for x in input()]
marked1 = [False for i in range(n)]
marked2 = marked1.copy()
flicks_g = 0
saves = 0
for i in range(n):
    idx1 = idx2 = -1
    val1 = val2 = (1 << 30)
    for j in range(n):
        if (m[j] > s[i] and m[j] < val1 and not marked1[j]):
            idx1 = j
            val1 = m[j]
        if (m[j] >= s[i] and m[j] < val2 and not marked2[j]):
            idx2 = j
            val2 = m[j]
    if (idx1 != -1):
        marked1[idx1] = True
        flicks_g += 1
    if (idx2 != -1):
        marked2[idx2] = True
        saves += 1
flicks_t = n - saves
print("%d\n%d" % (flicks_t, flicks_g))
