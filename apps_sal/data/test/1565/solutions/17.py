n = int(input())
a = input()
l = (n - 1) // 2
r = n // 2
while(a[l] == '0' and a[r] == '0'):
    l -= 1
    r += 1

# print(l)
# print(r)
ans = -1

if(a[l] != '0' and l > 0):
    x = int(a[0:l])
    y = int(a[l:len(a)])
    if(ans == -1 or ans > (x + y)):
        ans = x + y

if(a[r] != '0'):
    x = int(a[0:r])
    y = int(a[r:len(a)])
    if(ans == -1 or ans > x + y):
        ans = x + y

l -= 1
r += 1


if(l > 0 and a[l] != '0'):
    x = int(a[0:l])
    y = int(a[l:len(a)])
    if(ans == -1 or ans > (x + y)):
        ans = x + y

if(r < len(a) and a[r] != '0'):
    x = int(a[0:r])
    y = int(a[r:len(a)])
    if(ans == -1 or ans > x + y):
        ans = x + y

print(ans)
