# Codeforces 262 Div. 2
# P1

l = input().split()
n = int(l[0])
m = int(l[1])

c = 0
p = 1
while n != 0:
    n -= 1
    if p == m:
        n += 1
        p = 1
    else:
        p += 1
    c += 1
    
print(c)

