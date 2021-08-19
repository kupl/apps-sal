(n, m, r) = [int(i) for i in input().split(' ')]
s = [int(i) for i in input().split(' ')]
b = [int(i) for i in input().split(' ')]
s.sort()
b.sort()
if b[-1] >= s[0]:
    print(r // s[0] * (b[-1] - s[0]) + r)
else:
    print(r)
