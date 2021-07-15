S = input()

cs = [0]
r = 1
for c in S[::-1]:
    cs.append((cs[-1] + r*int(c)) % 2019)
    r *= 10
    r %= 2019

from collections import Counter
ctr = Counter(cs)
ans = 0
for v in ctr.values():
    ans += v*(v-1)//2
print(ans)
