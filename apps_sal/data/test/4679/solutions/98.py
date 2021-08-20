from collections import deque
sa = input()
sb = input()
sc = input()
q = deque(sa[0])
sa = sa[1:]
while q:
    t = q.pop()
    if t == 'a':
        if not sa:
            ans = 'A'
            break
        q.append(sa[0])
        sa = sa[1:]
    elif t == 'b':
        if not sb:
            ans = 'B'
            break
        q.append(sb[0])
        sb = sb[1:]
    elif t == 'c':
        if not sc:
            ans = 'C'
            break
        q.append(sc[0])
        sc = sc[1:]
print(ans)
