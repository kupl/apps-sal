n = int(input())
l = [2, 1]
for i in range(n-1):
    L = l[i] + l[i+1]
    l.append(L)
print(l[n])
