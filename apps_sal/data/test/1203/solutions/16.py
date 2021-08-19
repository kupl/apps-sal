h, l = list(map(int, input().split()))
print((l**2 - h**2) / (2 * h))


# x+h = sqrt(x2 + l2)
# h2 + 2xh = l2
# 2xh = l2 - h2
# x = (l2 - h2) / 2h
