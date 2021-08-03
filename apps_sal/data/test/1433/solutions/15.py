def calc(s, length):
    l = s.find('1')
    if l == -1:
        return 0
    r = s.rfind('1')
    return l + length - 1 - r + 2 * sum(s[i] == '0' for i in range(l + 1, r))


n, m = list(map(int, input().split()))
dp = []
num = 0
for i in range(n):
    dp.append(''.join(input().split()))
    num += calc(dp[i], m)

num += sum((calc(''.join(dp[i][j] for i in range(n)), n) for j in range(m)))

print(num)
