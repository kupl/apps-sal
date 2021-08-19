A, B = list(map(int, input().split()))
h = w = 100
ans = [['' for _ in range(w)] for __ in range(h)]
for i in range(h // 2):
    for j in range(w):
        if i & 1 and j & 1 and A - 1 > 0:
            ans[i][j] = '.'
            A -= 1
        else:
            ans[i][j] = '#'
for i in range(h - 1, h // 2 - 1, -1):
    for j in range(w):
        if i & 1 and j & 1 and B - 1 > 0:
            ans[i][j] = '#'
            B -= 1
        else:
            ans[i][j] = '.'

print((h, w))
for r in ans:
    print((''.join(r)))
