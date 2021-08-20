import sys
input = sys.stdin.readline
(N, K) = (int(x) for x in input().rstrip('\n').split())
vs = [int(x) for x in input().rstrip('\n').split()]
g = [vs[0], vs[-1]]
rest = K
for k in [K - 1, K]:
    for b in range(K // 2):
        t = k - b
        if t > N:
            t = N
        for i in range(t + 1):
            v = []
            if i < t:
                v.extend(vs[:i])
                v.extend(vs[-(t - i):])
                for _ in range(b):
                    if min(v) < 0:
                        v.remove(min(v))
                    else:
                        break
            else:
                v.extend(vs[:t])
                for _ in range(b):
                    if min(v) < 0:
                        v.remove(min(v))
            g.append(sum(v))
if max(g) < 0:
    print(0)
else:
    print(max(g))
