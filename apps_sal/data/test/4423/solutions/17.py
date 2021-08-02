N = int(input())
lst = []
for _ in range(N):
    S, P = input().split()
    lst.append([S, int(P)])
dct = dict(enumerate(lst))
lst2 = sorted(lst)

dct2 = {}
for n in lst2:
    if not n[0] in dct2:
        dct2[n[0]] = []
        dct2[n[0]].append(n[1])
    else:
        dct2[n[0]].append(n[1])

for m in dct2.keys():
    dct2[m] = sorted(dct2[m], reverse=True)

lst3 = []
for x in dct2.keys():
    for y in dct2[x]:
        lst3.append([x, y])

for i in lst3:
    for k, v in dct.items():
        if i == v:
            print(k + 1)
