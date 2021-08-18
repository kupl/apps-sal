n, m, d = map(int, input().split())
a = []
sum = 0
for i in range(n):
    a.extend(list(map(int, input().split())))
x = a[0] % d
a.sort()
mid = a[n * m // 2]
for i in a:
    if i % d != x:
        print('-1')
        return
    else:
        sum += abs(i - mid) // d
print(sum)
