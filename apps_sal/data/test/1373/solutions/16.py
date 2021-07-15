n, k = list(map(int, input().split()))
cnt = 0

for i in range(k, n + 2):
    minimum = (i - 1) * i // 2
    maximum = (2 * n - i + 1) * i // 2
    cnt += maximum - minimum + 1
    cnt %= 10 ** 9 + 7

print(cnt)
