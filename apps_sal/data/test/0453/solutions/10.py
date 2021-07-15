v = input().split('+')
a = len(v[0])
v = v[1].split('=')
b = len(v[0])
c = len(v[1])

def good(a, b, c):
    return a+b==c and a>0 and b>0 and c>0

if good(a-1, b, c+1):
    a = a-1
    c = c+1

if good(a, b-1, c+1):
    b = b-1
    c = c+1

if good(a+1, b, c-1):
    a = a+1
    c = c-1

if good(a, b+1, c-1):
    b = b+1
    c = c-1

if a+b==c:
    print('|'*a+'+'+'|'*b+'='+'|'*c)
else:
    print("Impossible")

