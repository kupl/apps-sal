n = int(input())
a = list(map(int, input().split()))
x = [0] * n
s1 = sum(a)
s2 = 0
for i in range(1, n - 1, 2):
    s2 += a[i]

x[0] = s1 - s2 * 2

for i in range(1, n):
    x[i] = -x[i - 1] + 2 * a[i - 1]

x = [str(a) for a in x]
x = ' '.join(x)
print(x)
