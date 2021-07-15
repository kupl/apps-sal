n = int(input())
a = list(map(int, input().split()))[1:]
b = list(map(int, input().split()))[1:]

used = set()
cnt = 0
while len(a) != 0 and len(b) != 0:
    if (tuple(a), tuple(b)) not in used:
        used.add((tuple(a), tuple(b)))
    else:
        print(-1)
        return
    x, y = a.pop(0), b.pop(0)
    if x > y:
        a.append(y)
        a.append(x)
    else:
        b.append(x)
        b.append(y)
    cnt += 1
print(cnt, '1' if len(b) == 0 else '2')

