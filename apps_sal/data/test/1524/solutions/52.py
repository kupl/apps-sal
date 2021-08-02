s = input()


def RLE(s):
    i, j = 0, 1
    ret = []
    while i < len(s):
        while j < len(s) and s[i] == s[j]:
            j += 1
        ret.append((s[i], j - i))
        i = j
    return ret


rle = RLE(s)
ans = []
for t in range(0, len(rle) - 1, 2):
    _, r = rle[t]
    _, l = rle[t + 1]
    for i in range(r - 1):
        ans.append(0)
    ans.append((r + 1) // 2 + l // 2)
    ans.append(r // 2 + (l + 1) // 2)
    for i in range(l - 1):
        ans.append(0)
print(' '.join(map(str, ans)))
