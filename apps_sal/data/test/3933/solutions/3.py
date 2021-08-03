n = int(input())
t = list(map(int, input().split(' ')))
s = set([])
for i in range(1, n):
    x = t[i] - t[i - 1]
    s.add(x)
if len(s) == 1:
    print(t[-1] + x)
else:
    print(t[-1])
