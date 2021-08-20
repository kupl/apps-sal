(n, k) = map(int, input().split())
p = [0]
maxx = 0
s = input().split()
for i in range(n):
    p.append(p[i] + int(s[i]))
for i in range(k, n + 1):
    for j in range(1, n - i + 2):
        if maxx < (p[j + i - 1] - p[j - 1]) / i:
            maxx = (p[j + i - 1] - p[j - 1]) / i
print(maxx)
