n = sum(list(map(int, input().split())))
print(-1 if n % 5 or n == 0 else n // 5)
