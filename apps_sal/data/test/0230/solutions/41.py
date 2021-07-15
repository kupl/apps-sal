n = int(input())
s = input()

def search(x):
    d = set()
    for i in range(n-2*x+1):
        d.add(s[i:i+x])
        if s[i+x:i+2*x] in d:
            return True
    return False

l = 0
r = n//2+1
while r > l+1:
    mid = (r+l)//2
    if search(mid):
        l = mid
    else:
        r = mid
print(l)
