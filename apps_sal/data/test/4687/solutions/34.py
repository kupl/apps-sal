l = [*map(int, open(c := 0).read().split())]
for a, b in sorted(zip(l[2::2], l[3::2])):
    if(c := c + b) >= l[1]:
        break
print(a)
