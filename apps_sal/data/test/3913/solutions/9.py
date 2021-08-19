n = int(input())
s = input()
e = set()
nbret = 0
for x in s:
    if x == '*':
        nbret += 1
    else:
        e.add(x)
m = int(input())

mini = nbret
L = []
for i in range(m):
    e1 = set()
    s1 = input()
    for k, x in enumerate(s1):
        if s[k] != "*" and x != s[k]:
            e1.clear()
            break
        if s[k] == '*' and x in e:
            e1.clear()
            break
        if s[k] == '*' and x not in e:
            e1.add(x)
    if len(e1) > 0:
        L.append(e1)
e = L[0]
maxi = len(e)
for i in range(1, len(L)):
    if len(L[i]) > maxi:
        maxi = len(L[i])
    e = e & L[i]

print(len(e))

# if len(e)==0:
#    if m==2:
#        print(maxi)
# else:
#    print(len(e))

# if len(e)>0 and len(e)<=nbret:

# else:
#   print(0)
