from collections import defaultdict

S = input()

d = defaultdict(int)

d[0] += 1

mod = 0
R = 1
for i in range(len(S)):
    mod = (mod + R * int(S[len(S) - i - 1])) % 2019
    R = R * 10 % 2019
    d[mod] += 1
ans = 0
for i in list(d.values()):
    if i > 1:
        ans += i * (i - 1) / 2

print((int(ans)))
