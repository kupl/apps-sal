from scipy.special import comb
n = int(input())
l = list(map(int, input().split()))
flg = [0 for i in range(2 * 10 ** 5 + 1)]
flg2 = [0 for j in range(2 * 10 ** 5 + 1)]
for i in l:
    flg[i] += 1
s = 0
for i in range(1, n + 1):
    flg2[i] += (flg[i] - 1) * (flg[i] - 2) / 2 - flg[i] * (flg[i] - 1) / 2
    s += flg[i] * (flg[i] - 1) / 2
for i in l:
    print(int(s + flg2[i]))
