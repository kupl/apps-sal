n = int(input())
a = list([ord(c)-97 for c in input()])
color = [0]*26
ans = [0]*n
last = -1

for i, c in enumerate(a):
    col = 0
    if last <= c:
        last = c
        if color[c] == 0:
            col = 1
        else:
            col = color[c] & (-color[c])
    else:
        col = 1
        for j in range(last, c, -1):
            while col & color[j]:
                col <<= 1

    color[c] |= col
    ans[i] = len(bin(col)) - 2

print(max(ans))
print(*ans)

