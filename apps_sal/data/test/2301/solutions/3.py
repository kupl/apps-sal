n = int(input())
a = sorted(map(int, input().split()))
l = [a[(1 - i % 2) * (n // 2) + i // 2]for i in range(n)]
c = 0
for i in range(1, n - 1):
    if l[i - 1] > l[i] < l[i + 1]:
        c += 1
print(c)
print(' '.join(map(str, l)))
