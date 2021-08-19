(n, x) = list(map(int, input().split()))
L = list(map(int, input().split()))
d = [0] * (n + 1)
cnt = 0
for i in range(n):
    d[i + 1] += d[i] + L[i]
for i in range(n + 1):
    if d[i] <= x:
        cnt += 1
print(cnt)
