k = int(input())
n = input()
l = []
s = 0
for i in range(len(n)):
    l.append(int(n[i]))
    s += int(n[i])
l.sort()
if s >= k:
    print(0)
else:
    term = 0
    while s < k:
        s += (9-l[term])
        term += 1
    print(term)

