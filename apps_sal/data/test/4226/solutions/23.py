(x, y) = list(map(int, input().split()))
haveAns = False
for i in range(1, x + 1):
    if i * 2 + (x - i) * 4 == y or i * 4 + (x - i) * 2 == y:
        print('Yes')
        haveAns = True
        break
if not haveAns:
    print('No')
