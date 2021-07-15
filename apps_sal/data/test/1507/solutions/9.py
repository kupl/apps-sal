n, k= input().split()
n, k= int(n), int(k)
s= input()
d= {}
f= {}
for i in range(65, 65+26):
    d[chr(i)]= 0
    f[chr(i)]= 0

for i in s:
    d[i]+=1

num= 0

for i in s:
    if(f[i]== 0):
        num+= 1
        if(num > k):
            print('YES')
            return
    f[i]+= 1
    if(f[i]== d[i]):
        num-= 1

print('NO')


