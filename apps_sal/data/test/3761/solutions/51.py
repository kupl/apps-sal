from collections import defaultdict as dd

s = input().strip()
n = len(s)
x, y = list(map(int, input().strip().split()))

stx = 0
while stx < n and s[stx] == "F":
    stx += 1

sty = 0

X, Y = list(range(2))

x_blocks = []
y_blocks = []
curr = 0
cdi = X

for i in range(stx, n):
    ch = s[i]
    if ch == "F":
        curr += 1
    else:
        if curr != 0:
            if cdi == X:
                x_blocks.append(curr)
            else:
                y_blocks.append(curr)
        curr = 0
        cdi = (cdi + 1) % 2
if curr != 0:
    if cdi == X:
        x_blocks.append(curr)
    else:
        y_blocks.append(curr)

curr = dd(int)
curr[stx] = 1

for xb in x_blocks:
    nxt = dd(int)

    for key in curr.keys():
        nxt[key + xb] += 1
        nxt[key - xb] += 1

    curr = nxt

if x not in curr:
    print("No")
    return

curr = dd(int)
curr[sty] = 1

for yb in y_blocks:
    nxt = dd(int)

    for key in curr.keys():
        nxt[key + yb] += 1
        nxt[key - yb] += 1

    curr = nxt

if y not in curr:
    print("No")
else:
    print("Yes")



