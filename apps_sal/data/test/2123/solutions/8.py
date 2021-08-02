# B
input()
e = 0
h = 0
r = 0
for x in [int(i) for i in input().split()]:
    t = x - h  # столько энергии требуется
    if e < t:
        r = r + (t - e)
        e = 0
    else:
        e = e - t
    h = x
print(r)
