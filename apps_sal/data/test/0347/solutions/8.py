def score(m, w, x):
    return max(0.3 * x, (1 - m / 250) * x - 50 * w)


m1, m2, m3, m4, m5 = (list(map(int, input().split())))
w1, w2, w3, w4, w5 = (list(map(int, input().split())))
hs, hu = (list(map(int, input().split())))
x1, x2, x3, x4, x5 = (500, 1000, 1500, 2000, 2500)
print(round(score(m1, w1, x1) + score(m2, w2, x2) + score(m3, w3, x3) + score(m4, w4, x4) + score(m5, w5, x5)) + 100 * hs - 50 * hu)
