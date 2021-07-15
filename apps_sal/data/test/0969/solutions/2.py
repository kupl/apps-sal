import sys
s = input()
l = len(s)
s_r = s[::-1]
t = input()
lent = len(t)
res = 0
tracks = []
step = 0    
while step < lent:
    if t[step:step+1] not in s:
        print(-1)
        return
        
    plus = 1
    while (t[step:step+plus] in s or t[step:step+plus] in s_r) and step + plus < lent+1:
        plus+=1
        
    
    if t[step:step+plus-1] in s:
        x = s.find(t[step:step+plus-1])
        #print(x, t[step:step+plus-1],step)
        tracks.append((x+1, x + plus-1))
    else:
        x = s_r.find(t[step:step+plus-1])
       # print(x, t[step:step+plus-1])
        tracks.append((l-x, l-x-plus+2))
    res+=1
    step+=plus-1
    
print(res)
for a, b in tracks:
    print(a, b)
