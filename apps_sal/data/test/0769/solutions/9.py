import sys
a, b, c = list(map(int, input().split()))
if a // b:
    a %= b
p = 0
pp = [0] * 10
i = 0
while p < 10:   
    i += 1
    a %= b
    a *= 10     
    if i > 100000:
        break
    if a // b == c:
        print(i)
        return
    if pp[a // b] == 0:
        pp[a // b] = 1
        p += 1 
print(-1)
    

