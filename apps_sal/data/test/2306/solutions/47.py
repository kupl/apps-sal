n = int(input())
t = list(map(int, input().split()))
T = [-1, 0]
for i in range(n):
    T.append(T[-1] + t[i])
T.append(T[-1] + 1)
V = [0] + list(map(int, input().split())) + [0]
VV = [110] * (2 * T[-1] + 1)
for i in range(n + 2):
    for j in range(2 * T[-1] + 1):
        if j < 2 * T[i]:
            a = T[i] - j / 2
            VV[j] = min(VV[j], a + V[i])
        elif 2 * T[i] <= j and j <= 2 * T[i + 1]:
            VV[j] = min(VV[j], V[i])
        else:
            a = j / 2 - T[i + 1]
            if a > 100:
                break
            VV[j] = min(VV[j], a + V[i])
print(sum(VV) / 2)
