
n, k = list(map(int, input().split()))
L = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    L[i].append(i)

L.sort(key=lambda x: x[1])


def c(x):
    for i in range(x[0], x[1] + 1):
        if T[i] >= k:
            return 0
    return 1


ans = 0
A = []
T = [0] * 203
i = 0
t = 0
while i < n:
    if c(L[i]) == 1:
        for j in range(L[i][0], L[i][1] + 1):
            T[j] += 1
        t = L[i][0]
    else:
        A.append(L[i][2] + 1)
        ans += 1

    i += 1
A.sort()
print(ans)
print(" ".join([str(i) for i in A]))
