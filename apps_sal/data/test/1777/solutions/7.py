cs = int(input())
open = []
clos = []
val = 0
for c in range(cs):
    brac = input()
    s = []
    for b in brac:
        if len(s) == 0 or b == '(':
            s.append(b)
        elif s[-1] == '(':
            s.pop()
        else:
            s.append(')')
    if len(s) != 0:
        if s[0] == s[-1] == '(':
            open.append(len(s))
        if s[0] == s[-1] == ')':
            clos.append(len(s))
    else:
        val += 1
close = dict()
for cl in clos:
    if cl not in close:
        close[cl] = 1
    else:
        close[cl] += 1
ans = val // 2
for op in open:
    if op in close:
        ans += 1
        close[op] -= 1
        if close[op] == 0:
            del close[op]
print(ans)
