s = input()

i1 = s.find('AB')
i2 = s.find('BA')
found = False
if i1 >= 0:
    i3 = s.find('BA', i1 + 2)
    if i3 != -1:
        print("YES")
        found = True
if not found and i2 >= 0:
    i3 = s.find('AB', i2 + 2)
    if i3 != -1:
        print("YES")
        found = True
if not found:
    print("NO")
