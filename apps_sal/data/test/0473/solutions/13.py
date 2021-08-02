h, m = [int(x) for x in input().split(":")]
hdiff, mdiff = [int(x) for x in input().split(":")]

m1 = m - mdiff
h1 = h - hdiff
if m1 < 0:
    m1 = 60 + m1
    h1 = h1 - 1
if h1 < 0:
    h1 = 24 + h1
h1 = str(h1)
m1 = str(m1)
print(h1.zfill(2) + ":" + m1.zfill(2))
