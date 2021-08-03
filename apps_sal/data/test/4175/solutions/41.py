N = int(input())
W = [input() for _ in range(N)]

d = dict()
last = W[0][0]

good = True
for w in W:
    if d.get(w) != None:
        good = False
        break
    elif w[0] != last:
        good = False
        break
    else:
        d[w] = 1
        last = w[-1]

if good:
    print("Yes")
else:
    print("No")
