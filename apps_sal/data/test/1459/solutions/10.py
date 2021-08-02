n, d = int(input()), list(map(int, input().split()))
a, b = map(int, input().split())
temp = min(a, b)
b = max(a, b)
a = temp
print(min(sum(d[a - 1:b - 1]), sum(d[b - 1:] + d[0:a - 1])))
