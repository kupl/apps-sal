from itertools import groupby
N = int(input())
s = input()
S = input()
mod = 10 ** 9 + 7
s = [len(list(j)) for (i, j) in groupby(s)]
ans = 3 * s[0]
for i in range(1, len(s)):
    if s[i - 1] == 1:
        ans *= 2
    elif s[i] == 2:
        ans *= 3
    ans %= mod
print(ans)
