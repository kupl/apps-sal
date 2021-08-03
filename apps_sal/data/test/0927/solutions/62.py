n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

a.sort(reverse=True)
num_of_matches = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [-1] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    val = -1
    for aa in a:
        if i - num_of_matches[aa] < 0:
            continue
        if i - num_of_matches[aa] == 0:
            val = 1
        elif dp[i - num_of_matches[aa]] > 0:
            val = max(val, dp[i - num_of_matches[aa]] + 1)
    dp[i] = val

res = ''
remain = dp[n]
match = n
while match > 0:
    for i in range(m):
        if match - num_of_matches[a[i]] >= 0 and remain - 1 == dp[match - num_of_matches[a[i]]]:
            match -= num_of_matches[a[i]]
            remain -= 1
            res += str(a[i])
            break
print(res)
