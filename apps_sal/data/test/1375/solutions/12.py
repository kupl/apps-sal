n = int(input())
t = [0] + list(map(int, input().split()))
for i in range(n): t[i + 1] += t[i]
p = [0] * (n + 1)
s = t[-1]
a = s // 3
b = s - a
if s == 3 * a:
    for i in range(1, n - 1):
        p[i] += p[i - 1]
        if t[i] == a: p[i] += 1
print(sum(p[i] for i in range(1, n - 1) if t[i + 1] == b))
