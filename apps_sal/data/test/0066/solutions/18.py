# your code goes here

[t, w, b] = [int(x) for x in input().split()]

def gcd(a, b):
    if (b==0):
        return a
    else:
        return gcd(b, a%b)

d = w*b // gcd(w, b)
m = min(w, b)

dint = t // d

count = m * dint

count += m - 1
    
d = dint * d + m - 1

if (d > t):
    count -= (d - t)

gcdtcnt = gcd(t, count)
t = t // gcdtcnt
count = count // gcdtcnt

print(count, '/', t, sep='')
