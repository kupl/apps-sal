n = int(input())
hatsugen = []
w = input()
hatsugen.append(w)
oshiri = w[-1]
Flag = True
for _ in range(n - 1):
    w = input()
    if w[0] != oshiri:
        Flag = False
        break
    if w in hatsugen:
        Flag = False
        break
    oshiri = w[-1]
    hatsugen.append(w)
if Flag:
    print('Yes')
else:
    print('No')
