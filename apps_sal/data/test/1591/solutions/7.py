(n, k) = list(map(int, input().split()))
favdrs = [0] * (k + 1)
for i in range(n):
    temp = int(input())
    favdrs[temp] += 1
num = 0
for i in range(k + 1):
    if favdrs[i] % 2 == 1:
        num += 1
print(n - num // 2)
