(n, k) = list(map(int, input().split()))
s = input()
ans = 0
zeroes = 0
zeroIndices = []
ind = 0
lastZero = -1
for i in range(len(s)):
    if s[i] == '1' and i > 0 and (s[i - 1] == '0') or (i == len(s) - 1 and s[i] == '0' and (len(s) > 1)):
        zeroIndices.append(i - 1)
        if zeroes == k:
            lastZero = zeroIndices[ind]
            ind += 1
        else:
            zeroes += 1
    if i == len(s) - 1 or (s[i] == '1' and s[i + 1] == '0'):
        ans = max(ans, i - lastZero)
print(ans)
