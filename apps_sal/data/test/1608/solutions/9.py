N = 10 ** 5 + 5
MOD = 10 ** 9 + 7
freq = [0 for i in range(N)]
p2 = [0 for i in range(N)]
p2[0] = 1
for i in range(1, N):
    p2[i] = p2[i - 1] * 2
    p2[i] %= MOD


def Calculate_Mobius(N):
    arr = [1 for i in range(N + 1)]
    prime_count = [0 for i in range(N + 1)]
    mobius_value = [0 for i in range(N + 1)]
    for i in range(2, N + 1):
        if prime_count[i] == 0:
            for j in range(i, N + 1, i):
                prime_count[j] += 1
                arr[j] = arr[j] * i
    for i in range(1, N + 1):
        if arr[i] == i:
            if prime_count[i] & 1 == 0:
                mobius_value[i] = 1
            else:
                mobius_value[i] = -1
        else:
            mobius_value[i] = 0
    return mobius_value


mobius = Calculate_Mobius(N)
n = int(input())
b = [int(i) for i in input().split()]
for i in b:
    freq[i] += 1
ans = 0
for i in range(1, N):
    cnt = 0
    for j in range(i, N, i):
        cnt += freq[j]
    total_subsequences = p2[cnt] - 1
    ans = (ans + mobius[i] * total_subsequences % MOD) % MOD
ans += MOD
print(ans % MOD)
