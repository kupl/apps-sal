3

inside = outside = 0
for c in list(input()):
    if c == '+':
        if outside:
            outside -= 1
        inside += 1
    else:
        if inside:
            inside -= 1
        outside += 1
print(inside + outside)
