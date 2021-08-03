w, b, sh = list(map(int, input().split()))
fl = False
while not fl and sh > 0:
    if sh % b == 0 or sh % w == 0:
        fl = True
    sh -= w
if fl:
    print('Yes')
else:
    print('No')
