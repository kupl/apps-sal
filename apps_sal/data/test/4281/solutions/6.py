n = int(input())
ar = list(map(int, input().split()))
used1 = [0] * (n + 3)
used2 = [0] * (n + 3)
ar.sort()
kol = 0
for i in range(n):
    if used1[ar[i] - 1] == 0:
        if used1[ar[i]] == 0:
            if used1[ar[i] + 1] == 0:
                kol += 1
                used1[ar[i]] = 1
                used1[ar[i] + 1] = 1
                used1[ar[i] - 1] = 1
print(kol, end=' ')
kol1 = 0
for i in ar:
    if used2[i - 1] == 0:
        kol1 += 1
        used2[i - 1] = 1
    elif used2[i] == 0:
        kol1 += 1
        used2[i] = 1
    elif used2[i + 1] == 0:
        kol1 += 1
        used2[i + 1] = 1
print(kol1)
