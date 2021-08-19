n = int(input())
ok = False
for i in range(1, 10):
    for j in range(1, 10):
        if n == j * i:
            ok = True
            break
if ok:
    print('Yes')
else:
    print('No')
