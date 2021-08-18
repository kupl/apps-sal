n, m, t = map(int, input().split())
k = [0] * m
while n:
    n -= 1
    s = input()
    for j in range(m):
        k[j] += s[j] == 'Y'
for i in k:
    n += i >= t
print(n)
