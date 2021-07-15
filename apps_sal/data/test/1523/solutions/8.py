n_k = input().split()
n = int(n_k[0])
k = int(n_k[1])
N = input().split()
T = input().split()
Svoboda = []
if len(set(N)) == n:
    s = 0
else:
    dict47 = {}
    j = 0
    for i in N:
        if i not in dict47:
            temp = {int(i): int(T[j])}
            dict47[i] = int(T[j])
        elif dict47.get(i) < int(T[j]):
            Svoboda.append(int(dict47.get(i)))
            dict47[i] = int(T[j])
        else:
            Svoboda.append(int(T[j]))
        j += 1
j = int(len(set(N)))
s = 0
Svoboda.sort()
for i in range(0, len(Svoboda)):
    if j < k:
        s += int(Svoboda[i])
        j += 1
print(s)
