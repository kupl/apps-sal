x, y, a, b, c = map(int, input().split())
rs = [int(i) for i in input().split()]
gs = [int(i) for i in input().split()]
ws = [int(i) for i in input().split()]

rs.sort(reverse=True)
gs.sort(reverse=True)
ws.sort(reverse=True)
weight = 0
rs = rs[:x]
rs = [0] + rs
gs = gs[:y]
gs = [0] + gs
ws = [0] + ws
r = 0
g = 0
w = 0
while r + g + w < x + y:
    if r < x:
        w1 = weight + rs[r + 1]
    else:
        w1 = 0
    if g < y:
        w2 = weight + gs[g + 1]
    else:
        w2 = 0
    if w < c:
        w3 = weight + ws[w + 1]
    else:
        w3 = 0
    weight = max(w1, w2, w3)
    if weight == w1:
        r += 1
    elif weight == w2:
        g += 1
    elif weight == w3:
        w += 1
print(weight)
