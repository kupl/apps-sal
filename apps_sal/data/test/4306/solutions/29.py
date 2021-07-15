a, b, c, d = tuple(map(lambda x: int(x), input().split(" ")))

start = max(a, c)
end = min(b, d)

print(max(end - start, 0))
