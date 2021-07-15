n = int(input())
s = input()
t = input()
lenS = len(s)
ta = []
tb = []
lenTa = lenTb = 0
res = []

for i in range(lenS):
    if s[i] != t[i]:
        if t[i] == 'a':
            ta.append(i)
            lenTa += 1
        else:
            tb.append(i)
            lenTb += 1

while lenTa > 1:
    res.append((ta[-1], ta[-2]))
    ta.pop()
    ta.pop()
    lenTa -= 2

while lenTb > 1:
    res.append((tb[-1], tb[-2]))
    tb.pop()
    tb.pop()
    lenTb -= 2

if lenTa and lenTb:
    res.append((ta[-1], ta[-1]))
    res.append((ta[-1], tb[-1]))
    
    print(len(res))
    
    for i in res:
        print(i[0]+1, i[1]+1)
elif lenTa or lenTb:
    print(-1)
else:
    print(len(res))
    
    for i in res:
        print(i[0]+1, i[1]+1)
