from math import log

x, y = list(map(int, input().split()))

a, b = y * log(x), x * log(y)

ans = '>' if a > b else '<' if a < b else '='
print(ans)
