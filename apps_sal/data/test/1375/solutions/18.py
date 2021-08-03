n = int(input())
lis = input().split()
for i in range(n):
    lis[i] = int(lis[i])
lis = [0] + lis
lis1 = [0]
for i in range(1, n + 1):
    lis1.append(lis1[i - 1] + lis[i])

if lis1[n] == 0:
    lis2 = []
    for i in range(1, n):
        if lis1[i] == 0:
            lis2.append(i)
    m = len(lis2)
    if m >= 2:
        print(int(m * (m - 1) / 2))
    else:
        print(0)
else:
    lis2 = []
    lis3 = []
    for i in range(n):
        if lis1[i] == lis1[n] / 3:
            lis2.append(i)
        if lis1[i] == lis1[n] * 2 / 3:
            lis3.append(i)
    m1 = len(lis2)
    m2 = len(lis3)
    if m1 >= 1 and m2 >= 1:
        lis4 = [0 for k in range(m1)]
        for i in range(m1):
            j = 0
            while j <= m2 - 1 and lis3[j] <= lis2[i]:
                j += 1
            lis4[i] = m2 - j
        print(sum(lis4))
    else:
        print(0)
