(n, m) = tuple(map(int, str.split(input())))
a = tuple(map(int, str.split(input())))
cbus = 0
count = 0
for x in a:
    if cbus + x <= m:
        cbus += x
    else:
        cbus = x
        count += 1
if cbus:
    count += 1
print(count)
