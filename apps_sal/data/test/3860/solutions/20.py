b = int(input())
g = int(input())
n = int(input())
if n < b and n < g:
    out = n + 1
elif n < b and g == n:
    out = n + 1 - n + b
elif n == b and g < n:
    out = n + 1 - n + g
elif n <= g:
    out = n + 1 - n + b
elif n <= b:
    out = n + 1 - n + g
else:
    out = n + 1 - n + g - n + b
print(out)
