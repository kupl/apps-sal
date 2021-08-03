n, x = list(map(int, input().split()))
a = []
d = {0: True}
d1 = [0]
if (x < (1 << n)):

    for t in range(1, 1 << n):

        if not d.get(t ^ x, False):
            a.append(t ^ d1[-1])
            d[t] = True
            d1.append(t)
    print(len(a))
    print(" ".join(map(str, a)))
else:
    for t in range(1, (1 << n)):

        a.append(t ^ (t - 1))
    print(len(a))
    print(" ".join(map(str, a)))
