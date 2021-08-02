n, m = map(int, input().split())
t = list(map(int, input().split()))
num = 0
for i in range(n - 1):
    if t[i + 1] - t[i] < m:
        num += t[i + 1] - t[i]
    else:
        num += m
print(num + m)
