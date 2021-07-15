def score(x):
    s = []
    for i in x:
        if len(s) == 0:
            s.append(i)
            continue
        h = s[-1]
        if h == '(' and i == ')':
            s.pop()
        else:
            s.append(i)
    if '(' in s and ')' in s:
        return None
    if '(' in s:
        return len(s)
    else:
        return -1 * len(s)

n = int(input())
a = []
for _ in range(n):
    x = input()
    a.append(x)
    
d = {}
for i in a:
    j = score(i)
    if j != None:
        if j in d:
            d[j] += 1
        else:
            d[j] = 1

c = 0
for i in d:
    if i == 0:
        c += d[i] // 2
    else:
        if -i in d and d[i] > 0 and d[-i] > 0:
            x = min(d[i], d[-i])
            d[i] -= x
            d[-i] -= x
            c += x
print(c)

