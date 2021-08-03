
H, W, M = list(map(int, input().split()))

h = [0] * H
w = [0] * W

hw = {}

for _ in range(M):
    a, b = list(map(int, input().split()))
    h[a - 1] += 1
    w[b - 1] += 1
    temp = "x" + str(a - 1) + "y" + str(b - 1)
    hw[temp] = 1

hm = max(h)
wm = max(w)

hp = [i for i, v in enumerate(h) if v == hm]
wp = [i for i, v in enumerate(w) if v == wm]

for x in hp:
    for y in wp:
        temp = "x" + str(x) + "y" + str(y)
        if temp not in hw:
            print((hm + wm))
            return
else:
    print((hm + wm - 1))
