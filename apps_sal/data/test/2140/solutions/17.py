s = [" "] + list(input())
n = len(s)
m = int(input())
a = [0] * (n // 2 + 10)
for x in input().split():
    a[int(x)] += 1
for i in range(1, n // 2 + 1):
    a[i] += a[i - 1]
for i in range(n // 2 + 1):
    if a[i] & 1:
        s[i], s[n - i] = s[n - i], s[i]
print(''.join(s[1:]))
