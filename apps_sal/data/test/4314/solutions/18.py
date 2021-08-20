(h, w) = map(int, input().split())
aa = [list(input()) for i in range(h)]
bb = list(zip(*aa))
cc = [b for b in bb if any((x == '#' for x in b))]
dd = list(zip(*cc))
ee = [d for d in dd if any((x == '#' for x in d))]
for i in range(len(ee)):
    print(''.join(ee[i]))
