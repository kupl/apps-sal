n = int(input())
ar = list(map(int, input().split()))
a1 = []
a2 = []
a3 = []
for i in range(len(ar)):
    if ar[i] == 1:
        a1.append(i + 1)
    if ar[i] == 2:
        a2.append(i + 1)
    if ar[i] == 3:
        a3.append(i + 1)
print(min(len(a1), len(a2), len(a3)))
for i in range(min(len(a1), len(a2), len(a3))):
    print(a1[i], a2[i], a3[i])

