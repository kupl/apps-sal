(h, w, k) = map(int, input().split())
Black = []
for i in range(h):
    c = input()
    for j in range(w):
        if c[j] == '#':
            Black.append((i, j))
ans = 0
for i in range(2 ** h):
    for j in range(2 ** w):
        a = len(Black)
        for b in Black:
            if i >> b[0] & 1 or j >> b[1] & 1:
                a -= 1
        if a == k:
            ans += 1
print(ans)
