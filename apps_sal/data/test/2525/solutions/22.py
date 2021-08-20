from collections import deque
s = input()
q = int(input())
a = 1
p = deque([s])
for _ in range(q):
    tfc = list(input().split())
    if tfc[0] == '1':
        a *= -1
    else:
        c = tfc[2]
        if tfc[1] == '1':
            if a == 1:
                p.appendleft(c)
            else:
                p.append(c)
        elif a == 1:
            p.append(c)
        else:
            p.appendleft(c)
print(''.join(p) if a == 1 else ''.join(p)[::-1])
