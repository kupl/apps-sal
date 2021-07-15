a = input().split(' ')
n = int(a[0])
m = int(a[1])
a = input().split(' ')
for i in range(n):
    a[i] = int(a[i])
pre = 0
while True:
    ans = -1
    for i in range(n):
        if a[i]>0:
            ans = i
            a[i] -= m
    if ans==-1:
        break
    pre = ans
print(pre+1)
