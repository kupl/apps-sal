o = list(input())
e = list(input())

lst = []
for oo, ee in zip(o, e):
    lst.append(oo + ee)

if len(o) - len(e) == 1:
    lst.append(o[-1])

print("".join(lst))
