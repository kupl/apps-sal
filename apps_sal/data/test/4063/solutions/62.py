n = int(input())
d = sorted(list(map(int, input().split())))

n = n // 2
print(d[n] - d[n-1])
