n = int(input())
single = []
double = []
titlesingle = []
titledouble= []
for i in range(n):
    x = input()
    l = list(x)
    titlesingle.extend(l)
    if len(x) > 1:
        for j in range(1, len(x)):
            s = x[j - 1] + x[j]
            titledouble.append(s)
sets = set(titlesingle)
setd = set(titledouble)
for i in range(26):
    s = chr(ord('a') + i)
    single.append(s)
for i in range(26):
    for j in range(26):
        s = chr(ord('a') + i) + chr(ord('a') + j)
        double.append(s)
if len(sets) < 26:
    ls = list(set(single) - sets)
    ls.sort()
    print(ls[0])
else:
    ls = list(set(double) - setd)
    ls.sort()
    print(ls[0])



