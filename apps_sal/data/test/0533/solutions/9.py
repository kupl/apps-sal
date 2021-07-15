a = int(input())
b = int(input())
x = int(input())
y = int(input())
n = int(input())
no = a*(x-1) + b*(y-1)
mn = 0
if n > no:
    mn = n-no
d = min(x,y)
e = max(x,y)
mx = 0
p = 0
q = 0
if d == x:
    p = a
    q = b
else:
    p = b
    q = a
if n <= p*d:
    mx = n//d
else:
    mx = (n-p*d)//e
    mx += p
print(mn,mx)
