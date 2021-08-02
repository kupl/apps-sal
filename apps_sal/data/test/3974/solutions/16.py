s = input()
inside = 0
outside = 0
seen = 0
for letter in s:
    if letter == '+':
        if outside == 0:
            inside += 1
            seen += 1
        else:
            inside += 1
            outside -= 1
    else:
        if inside == 0:
            outside += 1
            seen += 1
        else:
            outside += 1
            inside -= 1

print(seen)
