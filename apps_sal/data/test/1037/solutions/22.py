def main():
    a = int(input())
    nums = list(map(int, input().split()))
    vilist = []
    for i in range(a):
        vilist.append((nums[i], i))
    vilist = sorted(vilist, key=lambda vi: vi[0])
    dp = []
    for i in range(a):
        dp.append([0] * (a - i))
    for k in range(a - 1):
        vi = vilist.pop()
        v = vi[0]
        p = vi[1]
        vi_z = vilist[0]
        vz = vi_z[0]
        pz = vi_z[1]
        for i in range(k + 2):
            j = k - i + 1
            if k == a - 2:
                if j == 0:
                    dp[i][0] = dp[i - 1][0] + v * abs(p - i + 1) + vz * abs(pz - i)
                elif i == 0:
                    dp[0][j] = dp[0][j - 1] + v * abs(a - j - p) + vz * abs(a - j - 1 - pz)
                else:
                    dp[i][j] = max(dp[i - 1][j] + v * abs(p - i + 1) + vz * abs(pz - i), dp[i][j - 1] + v * abs(a - j - p) + vz * abs(pz - i))
            elif j == 0:
                dp[i][0] = dp[i - 1][0] + v * abs(p - i + 1)
            elif i == 0:
                dp[0][j] = dp[0][j - 1] + v * abs(a - j - p)
            else:
                dp[i][j] = max(dp[i - 1][j] + v * abs(p - i + 1), dp[i][j - 1] + v * abs(a - j - p))
    print(max([max(x) for x in dp]))


main()
