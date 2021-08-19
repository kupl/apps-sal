n = int(input())
l = [[int(j) for j in input().split()] for i in range(2)]
d1 = [0] * (n + 1)
d2 = [0] * (n + 1)
d1[0] = l[0][0]
d2[0] = l[1][0]
for i in range(1, n):
    d1[i] = max(d1[i - 1], d2[i - 1] + l[0][i])
    d2[i] = max(d2[i - 1], d1[i - 1] + l[1][i])
print(max(d1[n - 1], d2[n - 1]))
