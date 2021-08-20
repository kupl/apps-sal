n = int(input())
A = list(map(int, input().split()))
max_not_used = n
ones = []
twos = []
targets = []
failed = False
for (c, a) in zip(list(range(n, 0, -1)), reversed(A)):
    if a == 1:
        r = max_not_used
        max_not_used -= 1
        targets.append((r, c))
        ones.append((r, c))
    elif a == 2:
        if not ones:
            failed = True
            break
        else:
            (r, __) = ones.pop()
            targets.append((r, c))
            twos.append((r, c))
    elif a == 3:
        if not ones and (not twos):
            failed = True
            break
        else:
            if twos:
                (rr, cc) = twos.pop()
            else:
                (rr, cc) = ones.pop()
            r = max_not_used
            max_not_used -= 1
            targets.append((r, c))
            targets.append((r, cc))
            twos.append((r, c))
if failed:
    print(-1)
else:
    print(len(targets))
    for target in targets:
        print(*target)
