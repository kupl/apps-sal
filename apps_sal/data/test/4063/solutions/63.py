n = int(input())
d = list(map(int, input().split()))
d.sort()
x = d[n // 2 - 1]
y = d[n // 2]
print(y - x)
