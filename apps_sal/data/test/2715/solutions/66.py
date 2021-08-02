#Decrease (const)
K = int(input())
# 適当に構成する
N = 50
u, v = divmod(K, 50)
P = [u + i for i in range(N)]
for i in range(1, v + 1):
    P[-i] += 1
print(N)
print(*P)
