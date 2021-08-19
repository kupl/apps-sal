b = int(input())
g = int(input())
n = int(input())
x = y = 0
if n > b:
    x = n - b
if n > g:
    y = n - g
print(n + 1 - x - y)
