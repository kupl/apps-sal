f = [[1], [0, 1]]
n = int(input())
for i in range(2, n + 1):
    l = [0] + f[i - 1]
    for j in range(len(f[i - 2])):
        l[j] = l[j] + f[i - 2][j] & 1
    f.append(l)
print(n)
print(*f[n])
print(n - 1)
print(*f[n - 1])
