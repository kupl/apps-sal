w = input()
bea = True
elements = set(list(w))
for element in elements:
    if w.count(element) % 2 != 0:
        print('No')
        bea = False
        break
if bea:
    print('Yes')
