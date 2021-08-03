n, x = input().split()
n, x = int(n), int(x)
lis = []
for i in range(n):
    lis.append(input().split())
for i in range(n):
    for j in range(2):
        lis[i][j] = int(lis[i][j])
s = 0
for i in range(n):
    s += lis[i][1] - lis[i][0] + 1
s += (lis[0][0] - 1) % x
if n >= 2:
    for i in range(n - 1):
        s += (lis[i + 1][0] - lis[i][1] - 1) % x
print(s)
