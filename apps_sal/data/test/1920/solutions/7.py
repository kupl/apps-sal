DayM = [0 for i in range(367)]
DayF = [0 for i in range(367)]
n = int(input())
for i in range(n):
    a, b, c = input().split()
    Begin = int(b)
    End = int(c)
    for j in range(Begin, End + 1):
        if a == 'M':
            DayM[j] += 1
        else:
            DayF[j] += 1
M = 0
for i in range(367):
    m = min(DayM[i], DayF[i])
    if m > M:
        M = m
print(M * 2)
