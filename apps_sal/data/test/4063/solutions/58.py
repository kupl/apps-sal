N = int(input())
d = list(map(int, input().split()))
d.sort()
a = N // 2
print(d[a] - d[a - 1])
