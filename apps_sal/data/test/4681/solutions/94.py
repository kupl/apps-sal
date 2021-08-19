n = int(input())
l = [2, 1]
for i in range(2, n + 1):
    li = l[i - 1] + l[i - 2]
    l.append(li)
print(l[len(l) - 1])
