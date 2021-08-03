
x, a, b = list(map(int, input().split()))
print(("dangerous" if x < (b - a) else "safe" if a < b else "delicious"))
