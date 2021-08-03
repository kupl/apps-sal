l = list(input())
j = 0
c = 0
k = 0
l1 = 0
e = 0
p = 0
while(j < len(l)):
    if(l[j] == '+'):
        p += 1
        k += 1
    else:

        l1 += 1
        if(k >= e):
            c += (k - e)
            e = k

        k -= 1
        if(l1 > p):
            l1 -= 1
            c += 1

    j += 1
if(k > e):
    c += k - e

print(c)
