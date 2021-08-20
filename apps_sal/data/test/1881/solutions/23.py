(n, k) = list(map(int, input().split()))
p = list(map(int, input().split()))
processed = set()
color = {}
length = {}
ans = []
for i in range(n):
    elt = p[i]
    if elt in processed:
        ans.append(color[elt])
    else:
        processed.add(elt)
        new = 1
        run = True
        for j in range(1, k):
            if elt - j < 0:
                break
            elif elt - j not in processed:
                processed.add(elt - j)
                new += 1
            elif length[elt - j] + new <= k:
                for i2 in range(length[elt - j] + new):
                    color[elt - i2] = color[elt - j]
                length[elt] = length[elt - j] + new
                run = False
                break
            else:
                break
        if run:
            for j in range(new):
                color[elt - j] = elt - new + 1
            length[elt] = new
s = str(color[p[0]])
for elt in p[1:]:
    s += ' ' + str(color[elt])
print(s)
