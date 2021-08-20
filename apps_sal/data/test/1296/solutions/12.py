import sys
(n, s) = list(map(int, sys.stdin.readline().split()))
l = list(map(int, sys.stdin.readline().split()))
t = list([x[1] + n * (x[0] + 1) for x in enumerate(l)])
upper = n - 1
lower = 0
while upper > lower:
    k = (upper + lower) // 2
    t = list([x[1] + k * (x[0] + 1) for x in enumerate(l)])
    h = sum(sorted(t)[:k])
    if h == s:
        break
    if h < s:
        lower = k + 1
    else:
        upper = k - 1
t = list([x[1] + upper * (x[0] + 1) for x in enumerate(l)])
if sum(sorted(t)[:upper]) <= s:
    z = list([x[1] + (upper + 1) * (x[0] + 1) for x in enumerate(l)])
    if sum(sorted(z)[:upper + 1]) < s:
        print(upper + 1, sum(sorted(z)[:upper + 1]))
    else:
        print(upper, sum(sorted(t)[:upper]))
else:
    t = list([x[1] + (upper - 1) * (x[0] + 1) for x in enumerate(l)])
    print(upper - 1, sum(sorted(t)[:upper - 1]))
