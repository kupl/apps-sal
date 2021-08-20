n = input()
k = int(input())
l = len(n)
dp = [[[0] * 2 for j in range(k + 1)] for i in range(l + 1)]
dp[0][0][0] = 1
for i in range(l):
    ni = int(n[i])
    for j in range(k + 1):
        for st in range(2):
            for x in range(10):
                i_ = i + 1
                j_ = j
                st_ = st
                if x != 0:
                    j_ += 1
                if j_ > k:
                    continue
                if st_ == 0 and x > ni:
                    continue
                if st_ == 0 and x < ni:
                    st_ = 1
                dp[i_][j_][st_] += dp[i][j][st]
print(sum(dp[l][k]))
