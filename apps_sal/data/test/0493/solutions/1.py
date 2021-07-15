
n = int(input())
s = input().strip()

r = -1
l = -1
cb = 0
res = 0

for i in range(len(s)):
    if s[i] == ".":
        cb += 1
    elif s[i] == "L":            
        if r > -1:
            if cb % 2 == 1:
                res += 1
            cb = 0
        else:
            cb = 0
        r = -1
    else:
        if r > -1:
            cb = 0
            r = i
        else:        
            r = i
            res += cb
            cb = 0
        
if r == -1:
    res += cb
        
print(res)


