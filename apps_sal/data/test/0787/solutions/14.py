n = int(input())
s = input()
s1 = set()
ar = []
i = 0
prs = ''
j = 0
while len(ar) < n and i < len(s):
    ar.append(s[i])
    s1.add(s[i])
    i += 1
    while i < len(s) and s[i] in s1:
        ar[-1] += s[i]
        i += 1
    
    
if i < len(s):
    ar[-1] += s[i:]
if len(ar) < n:
    print('NO')
else:
    print('YES')
    for i in ar:
        print(i)
