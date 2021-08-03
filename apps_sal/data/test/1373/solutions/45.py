n, k = map(int, input().split())

cnt = []

for i in range(k, n + 2):
    cnt.append(i * n - (i - 1) * i + 1)

print(sum(cnt) % (10**9 + 7))
