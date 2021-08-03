n = int(input())
l = [int(x) for x in input().split()]
assert len(l) == n
l.reverse()
pre = [0]
for i in range(1, n):
    pre.append(max(pre[-1], l[i - 1]))
out = [max(0, 1 + pre[i] - l[i]) for i in range(n)]
out.reverse()
print(' '.join(str(x) for x in out))
