l = list(map(int, input().split()))
k = int(input())
i = l.index(max(l))
m = l[i]
del l[i]
l.append(m * 2 ** k)
print(sum(l))
