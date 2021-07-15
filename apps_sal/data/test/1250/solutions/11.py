n = int(input())
print(-1 if n < 3 else " ".join(map(str, [x for x in range(n, 0, -1)])))
