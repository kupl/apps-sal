s = input()
r = 0
l = 0
ls = [0]*len(s)
for i in range(len(s)):
    
    if s[i] == 'R':
        if l > 0 :
            left = (l+1)//2 + r//2
            right = l//2 + (r+1)//2
            ls[i-l] = left
            ls[i-l-1] = right
            r = 0
            l = 0
        r += 1
    else :
        l += 1
left = (l+1)//2 + r//2
right = l//2 + (r+1)//2
ls[len(s)-l] = left
ls[len(s)-l-1] = right
print((*ls))

