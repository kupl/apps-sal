(n, m) = list(map(int, input().split()))
a = [list(input()) for i in range(n)]
ima = 0
jma = 0
imi = n + 1
jmi = m + 1
for i in range(n):
    for j in range(m):
        if a[i][j] == '*':
            if i < imi:
                imi = i
            if i > ima:
                ima = i
            if j < jmi:
                jmi = j
            if j > jma:
                jma = j
if ima - imi + 1 > 0 and ima - imi + 1 >= jma - jmi + 1:
    print(ima - imi + 1)
elif jma - jmi + 1 > 0 and jma - jmi + 1 >= ima - imi + 1:
    print(jma - jmi + 1)
elif jma - jmi <= 0 and ima - imi <= 0:
    print(0)
