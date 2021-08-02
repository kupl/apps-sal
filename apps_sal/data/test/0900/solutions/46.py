from copy import copy

MOD = 10**9 + 7
s = input()
count = [0 for _ in range(13)]
count[0] = 1
for i in range(len(s)):
    new = [0 for _ in range(13)]
    for m in range(13):
        new[(m * 10) % 13] = count[m]
    count = new
    if s[i] != "?":
        div = int(s[i])
        count = count[-div:] + count[:-div]
    else:
        new = [0 for _ in range(13)]
        pre = sum(count[:3])
        SUM = sum(count) % MOD
        for j in range(13):
            pre += count[(j + 3) % 13]
            pre -= count[j % 13]
            new[j] = (SUM - pre) % MOD
        count = new
print(count[5])
