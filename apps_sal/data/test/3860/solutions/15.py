b = int(input())
g = int(input())
n = int(input())
if b >= n and g >= n:
    print(n + 1)
elif b >= n and g < n:
    print(g + 1)
elif g >= n and b < n:
    print(b + 1)
else:
    print(b + g - n + 1)
