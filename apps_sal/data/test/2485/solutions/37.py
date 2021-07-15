from collections import Counter

H, W, M = list(map(int, input().split()))
dh, dw = Counter(), Counter()
used = set()

for _ in range(M):
    h, w = list(map(int, input().split()))
    dh[h] += 1
    dw[w] += 1
    used.add((h, w))

ih = dh.most_common()
iw = dw.most_common()
s = ih[0][1] + iw[0][1]
ans = 0

for h, sh in ih:
    for w, sw in iw:
        if sh+sw < s or ans == s:
            break
        b = sh + sw - ((h, w) in used)
        ans = max(ans, b)
print(ans)

