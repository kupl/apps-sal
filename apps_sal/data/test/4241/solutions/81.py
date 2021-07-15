s = input()
t = input()
if t in s:
    print(0)
    return
r=0
for i in range(0,len(s)-len(t)+1):
    sub_str = s[i:i+len(t)]
    c=0
    for a,b in zip(sub_str,t):
        if a==b:
            c+=1
    r = max(r,c)
#     print(f'c={c}')
    if r == len(t)-1:
        break
print(len(t) - r)
