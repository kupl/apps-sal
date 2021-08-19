N = int(input())
P = list(map(int, input().split()))
S = sorted(P, reverse=True)
cn = 0
L = []
for i in range(N):
    if i == 0:
        cn = cn + 1
        L.append(P[i])
    elif P[i] > L[0]:
        continue
    else:
        cn = cn + 1
        L.append(P[i])
        L.pop(0)
print(cn)
