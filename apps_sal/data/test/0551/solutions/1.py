n = int(input())
a = list(map(int, input().split()))
anss = 0
for i in range(1, n):
    ans = 0
    k = -1
    m = -1
    j = 1
    while (k == -1 and j < n):
        if (i * (a[j] - a[0]) != j * (a[i] - a[0])):
            k = j
        j = j + 1
    while (j < n and m == -1):
        if (i * (a[j] - a[0]) != j * (a[i] - a[0])):
            if (i * (a[j] - a[k]) != (j - k) * (a[i] - a[0])):
                m = 1
        j = j + 1
    if (m == -1 and k != -1):
        anss = 1
if (anss == 1):
    print("Yes")
else:
    i = 0
    if ((i - 1) * (a[2] - a[1]) != a[i] - a[1]):
        anss = 1
    for i in range(3, n):
        if ((i - 1) * (a[2] - a[1]) != a[i] - a[1]):
            anss = -1
    if (anss == 1):
        print("Yes")
    else:
        print("No")
