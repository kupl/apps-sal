n = int(input())
a = list(map(int, input().split()))
s = [0]
for q in range(1, n // 2):
    s.append(s[-1] + max(0, a[q] - a[q - 1]))
for q in range(n // 2, n):
    s.append(a[n - q - 1] - s[n - q - 1])
print(*s)
