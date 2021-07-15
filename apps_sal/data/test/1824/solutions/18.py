def leng(x1, y1, x2, y2):
    return (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)
def check(x1, y1, x2, y2, x, y):
    return ((x - x1) / (x2 - x1) * (y2 - y1) + y1 >= y);
n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
d = {}
d1 = {}
for i in range(n):
    try:
        d[a[i]] += 1
    except:
        d[a[i]] = 1
for i in range(n - 1):
    try:
        d1[b[i]] += 1
    except:
        d1[b[i]] = 1  
    d[b[i]] -= 1
for i in range(n - 2):
    d1[c[i]] -= 1
for i in list(d.keys()):
    if (d[i] != 0):
        print(i)
        break
for i in list(d1.keys()):
    if (d1[i] != 0):
        print(i)
        break


    


