w = input()
f = True
for i in w:
    c = 0
    for k in w:
        if i == k:
            c += 1

    if c % 2 != 0:
        f = False
if not f:
    print("No")
else:
    print("Yes")
