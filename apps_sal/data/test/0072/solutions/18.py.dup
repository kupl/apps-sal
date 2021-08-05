n = int(input())
d1 = {}
d2 = {}
d3 = {}
s = input()
for i in s:
    try:
        d1[i] += 1
    except KeyError:
        d1[i] = 1
s = input()
for i in s:
    try:
        d2[i] += 1
    except KeyError:
        d2[i] = 1
s = input()
for i in s:
    try:
        d3[i] += 1
    except KeyError:
        d3[i] = 1
l = len(s)
n1 = -1
for i in d1:
    n1 = max(n1, d1[i])
n2 = -2
for i in d2:
    n2 = max(n2, d2[i])
n3 = -3
for i in d3:
    n3 = max(n3, d3[i])

if(n1 == l):
    if(n == 1):
        n1 -= 1
else:
    n1 = min(l, n1 + n)
if(n2 == l):
    if(n == 1):
        n2 -= 1
else:
    n2 = min(l, n2 + n)
if(n3 == l):
    if(n == 1):
        n3 -= 1
else:
    n3 = min(l, n3 + n)


if(n1 > n2 and n1 > n3):
    print("Kuro")
elif(n2 > n1 and n2 > n3):
    print("Shiro")
elif(n3 > n1 and n3 > n2):
    print("Katie")
else:
    print("Draw")
