n = int(input())
has = {}

def comp(e1):
    return e1[1]

for i in range(n):
    s = input()
    has[s]=i
ar = []
for k,v in has.items():
    ar.append([k,v])
ar.sort(key=comp, reverse=True)
for x in ar:
    print(x[0])
