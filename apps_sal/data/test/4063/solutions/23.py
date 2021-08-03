n = int(input())
d = list(map(int, input().split()))
d.sort()
print(len(range(d[n // 2 - 1], d[n // 2])))
