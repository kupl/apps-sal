s = input()
cs = ['']
ans = []
last = ['']
poped = False
for c in s[::-1]:
    if not poped and c == cs[-1] and (c > last[-2]):
        cs.pop()
        if not cs or c != cs[-1]:
            last.pop()
        poped = True
    else:
        poped = False
        if c != cs[-1]:
            last.append(c)
        cs.append(c)
    if len(cs) <= 11:
        ans.append((len(cs) - 1, ''.join(cs[::-1])))
    else:
        ans.append((len(cs) - 1, (''.join(cs[:3]) + '...' + ''.join(cs[-5:]))[::-1]))
for (a, b) in ans[::-1]:
    print(a, b)
