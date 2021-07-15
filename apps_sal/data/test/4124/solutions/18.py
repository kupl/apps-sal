s = input()
t = input()

c = 0
s=s[::-1]
t=t[::-1]
for i in range(min(len(s), len(t))):
    if s[i] == t[i]:
        c += 1
    else:
        break
        
print(len(s)+len(t)-2*c)             
    

