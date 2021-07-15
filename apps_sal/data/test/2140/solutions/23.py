s = list(input())
m = int(input())
a = list(map(int,input().split()))


x = len(s)
c = [0]*(x//2)
for i in range(m):
    c[a[i]-1]+=1
flag = 0
for i in range(1, x//2):
    c[i] += c[i-1]

for i in range(x//2):
    if c[i]%2!=0:
        s[i], s[x-i-1] = s[x-i-1], s[i]
print(''.join(map(str,s)))

