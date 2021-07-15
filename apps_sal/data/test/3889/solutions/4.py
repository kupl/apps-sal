n = int(input())
p = input()
d = {}
for c in p:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

if len(d) == 1:
    print("Yes")
else:
    for v in d.values():
        if v >= 2:
            print("Yes")
            return
    print("No")
