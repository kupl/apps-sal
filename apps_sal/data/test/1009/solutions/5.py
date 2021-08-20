import sys
line1 = sys.stdin.readline().split()
n = int(line1[0])
k = int(line1[1])
s = sys.stdin.readline().split()
s = [int(x) for x in s]
if n == 1:
    print(s[0])
else:
    pairs = s[:2 * n - 2 * k]
    pair_sums = []
    for i in range(int(len(pairs) / 2)):
        pair_sums.append(pairs[i] + pairs[-i - 1])
    if len(pair_sums) > 0:
        pmax = max(pair_sums)
    else:
        pmax = 0
    singles = s[-(2 * k - n):]
    if len(singles) > 0:
        smax = max(singles)
    else:
        smax = 0
    print(max(pmax, smax))
