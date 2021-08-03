L = int(input())

N = len(bin(L)[2:])
M = 2 * (N - 1) + bin(L)[3:].count("1")
print(N, M)

for i in range(1, N):
    print(i, i + 1, 0)
    print(i, i + 1, 2**(i - 1))

temp = L
for i in range(1, N):
    if bin(L)[-i] == "1":
        print(i, N, temp - 2**(i - 1))
        temp -= 2**(i - 1)
