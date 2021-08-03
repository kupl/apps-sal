lst = input()
lst = lst.split()


for i in range(len(lst)):
    lst[i] = int(lst[i])
N = lst[0]
L = lst[1]
q = L
l = 0
lste = [abs(L)]
tlst = []
for i in range(2, N + 1):
    t = L + i - 1
    q += t
    tlst.append(t)
    t = abs(t)
    lste.append(t)


slst = sorted(lste)
l = slst[0]
if tlst.count(-l) > 0:
    print(q + l)
else:
    print(q - l)
