n, m = input().split()
n = int(n)
m = int(m)
ban = [True] * (n + 1)
ban[0] = False
for i in range(m):
    L = input().split()
    L[0] = int(L[0])
    L[1] = int(L[1])
    ban[L[0]] = False
    ban[L[1]] = False

x = ban.index(True)

print(n - 1)

for i in range(1, n + 1):
    if(i == x):
        continue
    print(i, end=" " + str(x) + '\n')
