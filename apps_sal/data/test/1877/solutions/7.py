n = int(input())
s = input()
r = 0
u = 0
cst = 0
if s[0] == 'R': r+=1
else: u += 1
for i in range(1,n-1):
    if s[i] == 'R': r+=1
    else: u+=1
    if u == r and s[i]==s[i+1]:
        cst += 1
print(cst)

