n, k = [int(i) for i in input().split()]
col = [0 if d == "W" else 1 for d in input()]


offs = 0
if col[0] != col[-1]:
    offs = -1
    for i in range(n - 1):
        if col[i] == col[i + 1]:
            offs = i + 1
            break
    if offs == -1:
        if k % 2 == 0:
            print(''.join([["W", "B"][col[i]] for i in range(n)]))
        else:
            print(''.join([["B", "W"][col[i]] for i in range(n)]))
        return
    col = col[offs:] + col[:offs]

# print(col)
isalt = [0] * n
for i in range(1, n - 1):
    if col[i - 1] != col[i] and col[i] != col[i + 1]:
        isalt[i] = 1


sides = [[-1, -1] for i in range(n)]

ll = 0
for i in range(n):
    if isalt[i]:
        sides[i][0] = ll
    else:
        ll = i + 1
rr = 0
for i in range(n - 1, -1, -1):
    if isalt[i]:
        sides[i][1] = rr
    else:
        rr = i - 1


even = k % 2 == 0
ans = [0] * n
for i in range(n):
    if isalt[i] == 0:
        ans[i] = col[i]
    else:
        bb = sides[i]
        if i - bb[0] < bb[1] - i:
            dist = i - bb[0]
            nei = col[bb[0] - 1]
        else:
            dist = bb[1] - i
            nei = col[bb[1] + 1]
        if dist + 1 <= k:
            ans[i] = nei
        else:
            if even:
                ans[i] = col[i]
            else:
                ans[i] = 1 - col[i]


# print(ans)
if offs != 0:
    offs = n - offs
    ans = ans[offs:] + ans[:offs]

# print(offs, ans)

print(''.join([["W", "B"][ans[i]] for i in range(n)]))
