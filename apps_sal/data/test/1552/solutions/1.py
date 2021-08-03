n = int(input())
a = list(map(int, input().split()))
k1 = []
k2 = []
k3 = []

for i in range(n):
    if a[i] == 1:
        k1.append(i + 1)
    elif a[i] == 2:
        k2.append(i + 1)
    else:
        k3.append(i + 1)
k = min(len(k1), len(k2), len(k3))
print(k)
for i in range(k):
    print(k1[i], k2[i], k3[i])
