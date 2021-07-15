n = int(input())
a = [True]*1999
a1 = [0]*1999
b = [True]*1999
b1 = [0]*1999
ans = 0
for i in range(n):
    x,y = map(int,input().split())
    d = x - y
    s = x + y
    k = d + 999
    l = s - 2
    if a[k]:
        a[k] = False
        a1[k] += 1
    else:
        #print('!!!')
        ans += a1[k]
        a1[k] += 1
    if b[l]:
        b[l] = False
        b1[l] += 1
    else:
        #print('!!!')
        ans += b1[l]
        b1[l] += 1
#print(a)
#print(a1)
#print(b)
#print(b1)
print(ans)
