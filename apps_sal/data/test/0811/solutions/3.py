a,b = list(map(int,input().split()))
out = a
while a >= b:
    out += (a // b)
    a = (a // b) + (a % b)
print(out)

