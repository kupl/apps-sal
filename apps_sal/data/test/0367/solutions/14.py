import math
s1 = input()
s1 = ''.join(sorted(s1))
nen = 0
p = ""
np = ""
ot = ""
o = ""
i = 0
o1 = []
while i < len(s1):
    if i == len(s1) - 1:
        np = np + s1[i]
    elif s1[i] == s1[i + 1]:
        p = p + s1[i]
        i = i + 1
    else:
        np = np + s1[i]
    i = i + 1
d = math.ceil(len(s1) / 2)
if len(s1) % 2 == 0:
    ot = ot + p
    for i in range(0, int(len(s1) / 2) - len(p)):
        ot = ot + np[i]
    ot = ''.join(sorted(ot))
else:
    ot = ot + p
    for i in range(0, int(math.ceil(len(s1) / 2)) - 1 - len(p)):
        ot = ot + np[i]
        nen = i + 1
    ot = ''.join(sorted(ot))
    ot = ot + np[nen]

for i in range(0, d):
    o = o + ot[i]
if len(s1) % 2 == 0:
    for i in range(0, d):
        o1.append(ot[d - i - 1])
else:
    for i in range(0, d - 1):
        o1.append(ot[d - i - 2])
# for i in range(0, d-1):
#    o1.append(ot[d-i-1])
# print(p)
# print(np)
# print(ot)
# print(ot)
# print(o)
# print(o1)
print(o + ''.join(o1))
