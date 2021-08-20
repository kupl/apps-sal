n = int(input())
d = [int(str) for str in input().split()]
(s1, f1) = [int(str) - 1 for str in input().split()]
s = min(s1, f1)
f = max(s1, f1)
direct = sum(d[s:f])
revers = sum(d[f:] + d[:s])
if min(direct, revers) == 0 & f - s > 0:
    print(max(direct, revers))
else:
    print(min(direct, revers))
