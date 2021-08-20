import itertools
n = int(input())
a = list(map(int, input().split()))
m = max(a)
t = 10 ** 9 + 1
for i in a:
    if abs(i - m // 2) < t and i != m:
        t = abs(i - m // 2)
        s = i
print(m, s)
