k = int(input()) - 1

l = 1
c = 9
while k >= c * l:
    k -= c * l
    l += 1
    c *= 10

c = 10**(l - 1) + k // l
print(str(c)[k % l])
