O = input()
E = input()
s = ""

for so, se in zip(O, E):
    s += so + se

if len(list(O)) > len(list(E)):
    s += O[-1]
elif len(list(O)) < len(list(E)):
    s += E[-1]

print(*s, sep="")
