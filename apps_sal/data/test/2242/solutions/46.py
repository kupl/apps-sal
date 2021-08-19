from collections import Counter
S = input()
S = S + '0'
mod = 2019
p = [0] * mod
r = 0
d = 1
for s in S[::-1]:
    t = int(s) % mod
    r += t * d
    r %= mod
    d = d * 10 % mod
    p[r] += 1

# p.append(0)
#ans = 0
#c = Counter(p)
# for k,n in c.most_common():
#  if n > 1:
#    ans += 1
#  else:break

print(sum([i * (i - 1) // 2 for i in p]))
