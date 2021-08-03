n = int(input())
d = list(map(int, input().split()))
d.sort()
print(d[int(n / 2)] - d[int(n / 2 - 1)])
