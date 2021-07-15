n = int(input())
c1 = (n//7)*2
c2 = c1
k1 = n%7
k2 = k1-5
if k1 >= 2:
    c1 += 2
else:
    c1 +=k1
if k2 >= 0:
    c2 += k2
print(c2,c1)

