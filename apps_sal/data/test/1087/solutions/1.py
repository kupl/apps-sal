(n, k) = map(int, input().split())
al = list(map(int, input().split()))
dp = [n] * 41
for i in range(n):
    i_bit = bin(al[i])[2:]
    lenb = len(i_bit)
    for j in range(lenb - 1, -1, -1):
        dp[lenb - 1 - j] -= int(i_bit[j])
temp = k
res = 0
m = n // 2
for i in range(40, -1, -1):
    if dp[i] > m and 2 ** i <= temp:
        temp -= 2 ** i
        res += 2 ** i * dp[i]
    else:
        res += 2 ** i * (n - dp[i])
print(res)
