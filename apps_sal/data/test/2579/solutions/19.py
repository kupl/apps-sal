l,r,x,y,k = list(map(int,input().split()))




def samt(n):
    if k*n > r:
        return 1
    if k*n < l:
        return -1
    return 0

av , ox = x, y

while av < ox + 1:
    n = (av + ox) // 2
    s = samt(n)
    if s == -1:
        av = n + 1
    elif s == 1:
        ox = n - 1
    else:
        break

found = False
for n in range(av, ox + 1):
    if samt(n) == 0:
        found = True

if found:
    print("YES")
else:
    print("NO")



