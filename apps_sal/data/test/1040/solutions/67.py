n = int(input())
l = list(input())
t = []
for i in range(n):
    t.append(l[i])
    if len(t) >= 3 and t[-3:] == ['f', 'o', 'x']:
        for j in range(3):
            t.pop()
print(len(t))
