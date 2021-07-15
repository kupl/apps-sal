n = int(input())
a = list(map(lambda c: ord(c)-97, input()))
color = [0]*26
ans = [0]*n
last = -1

for i, c in enumerate(a):
    col = 0
    if last <= c:
        last = c
        if color[c] == 0 or color[c] == 3:
            col = 1
        else:
            col = color[c]
    else:
        for j in range(last, c, -1):
            if color[j] == 0:
                continue
            if color[j] == 3:
                print('NO')
                return
            if col == 0:
                col = color[j] ^ 3
            elif col & color[j]:
                print('NO')
                return

    color[c] |= col
    ans[i] = col-1

print('YES')
print(*ans, sep='')

