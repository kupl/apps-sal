n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])

def thanhloc(x):     #loai bo het factor 2 va 3
    while (x % 2 == 0):
        x = x //2
    while (x % 3 == 0):
        x = x //3
    return(x)

res = 'Yes'
a[0] = thanhloc(a[0])
#import pdb; pdb.set_trace()
for i in range(1,n):
    a[i] = thanhloc(a[i])
    if a[i] != a[i-1] :
        res = 'No'
        break

print(res)

