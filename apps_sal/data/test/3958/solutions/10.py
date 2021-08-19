s = input()
l = []
even = []
odd = []
f = 1
for i in range(len(s)):
    if s[i] == '0':
        if len(even) != 0:
            ind = even.pop()
            l[ind].append(i + 1)
            odd.append(ind)
        else:
            l.append([i + 1])
            odd.append(len(l) - 1)
    elif len(odd):
        ind = odd.pop()
        l[ind].append(i + 1)
        even.append(ind)
    else:
        f = 0
        break
if f and len(even) == 0:
    print(len(l))
    for x in l:
        print(len(x), *x)
else:
    print(-1)
