(n, m, k) = input().split(' ')
n = int(n)
m = int(m)
k = int(k)
l = [[0 for x in range(m + 2)] for x in range(n + 2)]
flag = 0
for i in range(k):
    (a, b) = input().split(' ')
    a = int(a)
    b = int(b)
    l[a][b] = 1
    if l[a][b + 1] == 1 and l[a - 1][b] == 1 and (l[a - 1][b + 1] == 1):
        if flag == 0:
            flag = i + 1
    elif l[a - 1][b] == 1 and l[a - 1][b - 1] == 1 and l[a][b - 1]:
        if flag == 0:
            flag = i + 1
    elif l[a][b - 1] == 1 and l[a + 1][b - 1] == 1 and l[a + 1][b]:
        if flag == 0:
            flag = i + 1
    elif l[a][b + 1] == 1 and l[a + 1][b] and l[a + 1][b + 1]:
        if flag == 0:
            flag = i + 1
print(flag)
