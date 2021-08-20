input()
power = list(map(int, input().split()))
n = len(power)
ps = [0] + sorted(range(1, n), key=lambda i: -power[i])
out = []
bonus = [0] * power[0]
i = 1
while i < n and bonus:
    out.append((bonus.pop(), ps[i]))
    bonus.extend([ps[i]] * max(0, power[ps[i]]))
    i += 1
if i != n:
    print(-1)
else:
    print(len(out))
    print(*['%s %s' % (a + 1, b + 1) for (a, b) in out], sep='\n')
