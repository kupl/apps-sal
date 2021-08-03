S = input()
just, over = 0, 1
for c in S:
    c = int(c)
    just, over = [
        min(just + c, over + (10 - c)),
        min(just + (c + 1), over + (9 - c))
    ]
print(just)
