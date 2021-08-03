n = int(input())
consec = 1
changes = 0
oppo = 0
rep = False
cons = False
s = input().strip()
prev = s[0]
for x in s[1:]:
    if prev != x:
        changes += 1
        consec = 1
        rep = False
    else:
        consec += 1
        if not rep:
            rep = True
            oppo += 1
    if consec == 3:
        cons = True
    prev = x
if cons or oppo > 1:
    changes += 2
elif oppo == 1:
    changes += 1
print(changes + 1)
