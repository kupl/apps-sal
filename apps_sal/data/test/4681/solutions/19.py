n = int(input())
l = [2, 1]

for i in range(85):
    l.append(l[-2] + l[-1])

print(l[n])
