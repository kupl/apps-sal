(N, K) = map(int, input().split())
numgcd = [0] * (K + 1)
sumgcd = 0
mod = 10 ** 9 + 7
for i in range(1, K + 1)[::-1]:
    numgcd[i] = pow(K // i, N, mod)
    count = 2
    while count * i <= K:
        numgcd[i] -= numgcd[count * i]
        count += 1
    sumgcd += numgcd[i] * i
print(sumgcd % mod)
