from collections import Counter
i1 = input()
i2 = input()
s1 = Counter(i1)
s2 = Counter(i2)
intersect = s1 & s2
s1.subtract(intersect)
s2.subtract(intersect)
opa = Counter(''.join(s1.elements()).lower()) & Counter(''.join(s2.elements()).lower())
print(sum(intersect.values()), sum(opa.values()))
