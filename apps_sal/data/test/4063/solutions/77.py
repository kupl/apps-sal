N = int(input()) // 2
d = sorted(list(map(int, input().split())))
print(d[N] - d[N - 1])
