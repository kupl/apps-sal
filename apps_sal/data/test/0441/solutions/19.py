(n, a, b) = list(map(int, input().strip().split()))
s = input().split('*')
rslt = 0
for segment in s:
    less = len(segment) // 2
    more = len(segment) - less
    x = 0
    y = 0
    if a > b:
        x = min(a, more)
        y = min(b, less)
    else:
        x = min(a, less)
        y = min(b, more)
    rslt += x + y
    a -= x
    b -= y
print(rslt)
