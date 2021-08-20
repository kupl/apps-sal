import re
(n, m, k) = map(int, input().split())
s = [input() for _ in range(n)]
if n > 1 and k > 1:
    t = list(map(lambda x: ''.join(x), zip(*s)))
    s += t
ans = 0
p = re.compile('\\.{' + str(k) + ',}')
for i in s:
    ans += sum(map(lambda x: len(x) - k + 1, p.findall(i)))
print(ans)
