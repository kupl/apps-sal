x, y = list(map(ord, input().split()))
print(("<" if x < y else ">" if x > y else "="))
