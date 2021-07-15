n, x, t = map(int,input().split())
result = n // x
# if n > x:
#     result += 1
if n % x == 0:
    result += 0
else:
    result += 1
print(int(result * t))
