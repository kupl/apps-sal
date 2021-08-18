import math
n, m, k = list(map(int, input().split()))
lst = [0] * m
res = [0] * m
ans = 0
otvet = 0
for i in range(m):
    lst[i] = int(input())

fed = int(input())
for i in range(m):
    res[i] = lst[i] ^ fed
    res[i] = bin(res[i])[2:]
    ans = 0
    for j in range(len(res[i])):

        if res[i][j] == '1':
            ans += 1

    if ans <= k:

        otvet += 1
print(otvet)
