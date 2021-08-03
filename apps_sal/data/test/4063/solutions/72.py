n = int(input())
d = list(map(int, input().split()))
c = 0
d.sort()
n = int(n / 2)

print(d[n] - d[n - 1])
