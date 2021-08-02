n = int(input())
a = list(map(int, input().split()))
a = [0] + a + [0]

max_fee = 0
for i in range(1, n + 2):
    max_fee += abs(a[i] - a[i - 1])

for i in range(1, n + 1):
    res = max_fee - abs(a[i] - a[i - 1]) - \
        abs(a[i + 1] - a[i]) + abs(a[i + 1] - a[i - 1])
    print(res)
