(a, b) = list(map(str, input().split()))
h = 'H'
d = 'D'
result = h
if a == h:
    if b == d:
        result = d
elif b == h:
    result = d
else:
    result = h
print(result)
