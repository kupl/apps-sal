N = int(input())
d = sorted([int(i) for i in input().split()])
print(d[N // 2] - d[N // 2 - 1])
