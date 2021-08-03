from collections import Counter
n, k = list(map(int, input().split()))
ar = list(map(int, input().split()))
kc = []
ris = 0
for cont in range(0, n - k + 1, k):
    kc.append(ar[cont:cont + k])
for cont in range(0, k):
    l = []
    for cont2 in range(0, len(kc)):
        l.append(kc[cont2][cont])
        a = Counter(l).most_common(1)[0][1]
    ris += len(kc) - a
print(ris)
