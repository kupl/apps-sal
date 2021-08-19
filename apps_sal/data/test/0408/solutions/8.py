(expert, newbie) = map(int, input().strip().split())
minn = min(expert, newbie)
maxx = max(expert, newbie)
counter = 0
while minn - 1 >= 0 and maxx - 2 >= 0:
    minn -= 1
    maxx -= 2
    if minn > maxx:
        (minn, maxx) = (maxx, minn)
    counter += 1
print(counter)
