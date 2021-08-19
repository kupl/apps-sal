n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
i = l.index(max(l))
l[i] = l[i] // 2
print(sum(l))
