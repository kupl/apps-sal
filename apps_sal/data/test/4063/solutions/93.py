n = int(input())
d = list(map(int, input().split()))
d.sort()
cnt = 0
if n % 2 != 0:
    print(0)
else:
    n = int(n / 2)
    print(d[n] - d[n - 1])
