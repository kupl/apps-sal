def read(): return list(map(int, input().split()))


n = int(input())
a = list(read())
a = [(a[i], i + 1) for i in range(n)]
a.sort()
for i in range(n // 2):
    print(a[i][1], a[n - i - 1][1])
