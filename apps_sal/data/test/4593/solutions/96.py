import math
X = int(input())
list1 = []

for i in range(2, X + 1):
    for j in range(2, int((X + 1) / 2)):
        a = math.log10(i) / math.log10(j)
        if a.is_integer():
            list1.append(i)
if list1 == []:
    print((1))
else:
    print((max(list1)))
