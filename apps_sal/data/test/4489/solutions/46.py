from collections import Counter
N = int(input())
blue = [input() for _ in range(N)]
M = int(input())
red = [input() for _ in range(M)]
Cb = Counter(blue)
Cr = Counter(red)
ans = 0
for b in Cb.most_common():
    x = b[0]
    y = b[1]
    if Cr.get(x):
        ans = max(ans, y - Cr[x])
    else:
        ans = max(ans, y)
print(ans)
