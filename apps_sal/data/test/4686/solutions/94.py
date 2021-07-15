w = input()
for c in set(w):
    if w.count(c) % 2:
        print('No')
        break
else:
    print('Yes')
