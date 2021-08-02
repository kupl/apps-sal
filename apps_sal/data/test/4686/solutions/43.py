a = input(); b = set(a)

for i in b:
    if a.count(i) % 2 != 0:
        print('No')
        return

print('Yes')
