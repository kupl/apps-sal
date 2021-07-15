def getVar(): 
    return tuple(map(int, input().split()))
n, m = getVar()
a = getVar()
b = getVar()
#print(a,b)
c = max(min(a) * 2, max(a))
#c = -1
d = min(b) - 1
if c > d:
    c = -1
print(c)

