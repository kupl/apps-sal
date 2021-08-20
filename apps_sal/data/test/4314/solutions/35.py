(H, W) = list(map(int, input().split()))
a = [list(input()) for i in range(H)]
a = [x for x in a if '#' in x]
aT = list(zip(*a))
aT = [x for x in aT if '#' in x]
a = list(zip(*aT))
for i in a:
    print(''.join(i))
