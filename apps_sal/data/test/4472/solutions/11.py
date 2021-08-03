n = int(input())
s1 = input()
s2 = input()

x = []
i = 0
j = n - 1
while i < j:
    x += [[s1[i], s1[j], s2[i], s2[j]]]
    i += 1
    j -= 1

count = 0
for elem in x:
    a1 = elem[0]
    a2 = elem[1]
    b1 = elem[2]
    b2 = elem[3]
    q = set(elem)
    if len(q) == 2:
        if len(set([a1, a2])) * len(set([b1, b2])) == 2:
            count += 1
    elif len(q) == 4:
        count += 2
    elif len(q) == 3:
        if a1 == b2 or a2 == b1 or a1 == b1 or a2 == b2 or b1 == b2:
            count += 1
        else:
            count += 2
if n % 2 == 1:
    if s1[i] != s2[i]:
        count += 1
print(count)
