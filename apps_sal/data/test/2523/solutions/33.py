s = input()
n = len(s)

l = 0
r = n//2 + 1

while r - l > 1:
    m = l + (r-l)//2
    d = n//2 - m
    if s[d:n-d].count("0") == 0 or s[d:n-d].count("1") == 0:
        l = m
    else:
        r = m

if n % 2 == 0:
    print((n//2+l))
else:
    print((n//2+l+1))

