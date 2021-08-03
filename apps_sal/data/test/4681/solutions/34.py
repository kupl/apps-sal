n = int(input())
l = [0 for i in range(n + 1)]
l[0] = 2
l[1] = 1
for j in range(2, n + 1):
    l[j] = l[j - 1] + l[j - 2]
print(l[n])
