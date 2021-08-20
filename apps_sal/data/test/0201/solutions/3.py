(c, hr, hb, wr, wb) = map(int, input().split())
s = 0
if wb < wr:
    (hr, hb, wr, wb) = (hb, hr, wb, wr)
if wb * wb > c:
    for nb in range(c // wb + 1):
        s = max(s, nb * hb + hr * ((c - wb * nb) // wr))
else:
    if hr * wb < hb * wr:
        (hr, hb, wr, wb) = (hb, hr, wb, wr)
    for nb in range(min(31625, c // wb + 1)):
        s = max(s, nb * hb + hr * ((c - wb * nb) // wr))
print(s)
