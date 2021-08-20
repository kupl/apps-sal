b = int(input())
g = int(input())
n = int(input())
b = min(n, b)
g = min(n, g)
mx = b
mn = 0
if g < n:
    mn = n - g
print(mx - mn + 1)
