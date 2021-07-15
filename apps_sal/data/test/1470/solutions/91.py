x = int(input())
q, r = divmod(x, 11)
q *= 2
if 1 <= r <= 6:
    q += 1
elif r > 6:
    q += 2
print(q)
