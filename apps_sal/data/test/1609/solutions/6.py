N = int(input())
things = list(map(int, input().split()))
ans = []
dif = set(things)
double = set()
to_zen = []
pnt = 0
for i in things:
    if i > N:
        dif.discard(i)
        to_zen += [pnt]
    elif i in double:
        to_zen += [pnt]
    double.add(i)
    pnt += 1
for i in range(1, N + 1):
    if i not in dif:
        things[to_zen.pop()] = i
        dif.add(i)
print(' '.join(list(map(str, things))))
