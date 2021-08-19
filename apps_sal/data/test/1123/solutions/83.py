MOD = 10 ** 9 + 7
(n, k) = map(int, input().split())
divisor_lst = [i - 1 for i in range(1, k + 1)]
divisor_lst[0] = 1
for i in range(2, k):
    for j in range(2 * i, k + 1, i):
        divisor_lst[j - 1] -= divisor_lst[i - 1]
ans = 0
for num in range(1, k + 1):
    ans += pow(k // num, n, MOD) * divisor_lst[num - 1]
    ans %= MOD
print(ans)
