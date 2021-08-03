n, s = list(map(int, input().split()))
a = list(map(int, input().split()))
s_a = sorted(a)
t = 0
for i in range(n - 1):
    t += s_a[i]
print('YES' if t <= s else 'NO')
