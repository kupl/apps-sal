N = int(input())
d = list(map(int, input().split()))
half = N // 2
d.sort()
print(d[half] - d[half - 1])
