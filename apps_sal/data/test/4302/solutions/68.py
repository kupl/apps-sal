a,b = map(int,input().split())
c = 0

if a > b:
    c = c + a
    a = a - 1

elif a < b:
    c = c + b
    b = b - 1

else:
    c = c + a

if a > b:
    c = c + a
    a = a - 1

elif a < b:
    c = c + b
    b = b - 1

else:
    c = c + a

print(c)
