from collections import Counter
s = input()
n = len(s)
digits = [int(c) for c in s[::-1]]
a = [0] * (n + 1)
p = 2019
for (i, digit) in enumerate(digits):
    a[i + 1] = (digit * pow(10, i, p) + a[i]) % p
counter = Counter(a)
ans = 0
for count in counter.values():
    ans += count * (count - 1) // 2
print(ans)
