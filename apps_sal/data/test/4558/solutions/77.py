

x, t = list(map(int, input().split()))

result = 0

if x > t:
    result = x - t
else:
    result = 0

print(result)
