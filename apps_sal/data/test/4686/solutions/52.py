w = input()
l = [chr(ord("a")+i) for i in range(26)]
for i in l:
    if w.count(i) % 2 != 0:
        print('No')
        return
print('Yes')
