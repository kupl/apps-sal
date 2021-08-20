(n, p) = list(map(int, input().split()))
p -= 1
if p >= n // 2:
    p = n - 1 - p
s = input()
d = [abs(ord(s[i]) - ord(s[n - 1 - i])) for i in range(n // 2)]
d = [min(x, 26 - x) for x in d]
(first, last) = (-1, -1)
for i in range(len(d)):
    if d[i] > 0:
        if first == -1:
            first = i
        last = i
a = 0 if first == -1 else min(abs(p - first), abs(p - last)) + (last - first) + sum(d)
print(a)
