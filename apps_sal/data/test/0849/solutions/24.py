a, b, c, d = input().split()
a, b, c, d = int(a), int(b), int(c), int(d)
print("%.12f" % ((a / b) * (1 / (1 - (1 - a / b) * (1 - c / d)))))
