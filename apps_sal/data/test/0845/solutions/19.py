def ff(x, i, d):
    n = x.find(i) + d
    if n<0:
        n=0
    if n==10:
        n=9
    return x[n]

c = input()
s = input()

d = 1 if c == 'L' else -1

x="qwertyuiop";
y="asdfghjkl;";
z="zxcvbnm,./";

ans = ""
for i in s:
    if x.find(i) != -1:
        ans += ff(x, i, d)
    if y.find(i) != -1:
        ans += ff(y, i, d)
    if z.find(i) != -1:
        ans += ff(z, i, d)
print (ans)
        
        

