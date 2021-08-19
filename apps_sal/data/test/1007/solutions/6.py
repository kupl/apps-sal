(K, P) = list(map(int, input().split()))
sums = 0
for i in range(1, K + 1):
    sums += int(str(i) + str(i)[::-1])
    sums %= P
print(sums)
