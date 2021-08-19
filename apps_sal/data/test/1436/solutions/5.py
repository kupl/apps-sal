input()
cops = 0
count = 0
for e in map(int, str.split(input())):
    if e == -1:
        if cops == 0:
            count += 1
        cops = max(0, cops - 1)
    else:
        cops += e
print(count)
