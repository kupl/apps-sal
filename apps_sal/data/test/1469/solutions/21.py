L = int(input())

Lbin = (bin(L)[2:])[::-1]
N = len(Lbin)
M = 2 * (N - 1) + Lbin.count("1") - 1
print(N, M)

for i in range(0, N - 1):
    print(i + 1, i + 2, 0)
    print(i + 1, i + 2, 2 ** i)

weight = L
for i in range(0, N - 1):
    if Lbin[i] == '1':
        weight -= 2 ** i
        print(i + 1, N, weight)
