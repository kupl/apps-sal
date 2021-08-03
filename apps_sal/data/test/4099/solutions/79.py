n, k, m = map(int, input().split())
a = tuple(map(int, input().split()))

total = sum(a)
for i in range(k + 1):
    if (total + i) / n >= m:
        print(i)
        return
print('-1')
