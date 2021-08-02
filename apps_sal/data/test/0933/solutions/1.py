given = input()
l = len(given)
typos = 0
yesno = [1 for _ in range(l)]
i = -1
while i < l - 1:
    i += 1
    cur = given[i]
    while i < l - 2 and cur == given[i + 1] == given[i + 2]:
        i += 1
        yesno[i] = 0

given = "".join([c for i, c in enumerate(given) if yesno[i] == 1])
l = len(given)
typos = 0
yesno = [1 for _ in range(l)]
i = 0
while i < l - 3:
    if given[i] == given[i + 1] and given[i + 2] == given[i + 3]:
        yesno[i + 2] = 0
        i += 3
    else:
        i += 1
print("".join([c for i, c in enumerate(given) if yesno[i] == 1]))
