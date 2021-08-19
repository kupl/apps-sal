(n, l) = map(int, input().split())
ringo = []
for i in range(l, l + n):
    ringo.append(i)
ringo.sort(key=int)
if 0 in ringo:
    print(sum(ringo))
else:
    if ringo[0] > 0:
        ringo.pop(0)
    else:
        ringo.pop(-1)
    print(sum(ringo))
