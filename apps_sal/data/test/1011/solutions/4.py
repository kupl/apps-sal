n, a = int(input()), list(map(int, input().split()))
m, b = int(input()), list(map(int, input().split()))

a.sort()
b.sort()

A, B = len(a) * 3, len(b) * 3
i = j = 0
tA, tB = A, B

while (i < len(a) and j < len(b)):
        d = min(a[i], b[j])
        while (i < len(a) and a[i] == d):
            i += 1
            tA -= 1
        while (j < len(b) and b[j] == d):
            j += 1
            tB -= 1
        if (tA - tB > A - B):
            A, B = tA, tB

if (j < len(b)):
    tB = len(b) * 2
    if (tA - tB > A - B):
        A, B = tA, tB

print(A, ':', B, sep = '')

    

