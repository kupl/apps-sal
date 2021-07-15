a, b, c, d = map(int, input().split())

r = 42

if b - a == c - b == d - c:
    r = d + b -a
if b / a == c / b == d / c and int(d * b / a) == d * b / a:
    r = int(d * c / b)
    
print(r)
