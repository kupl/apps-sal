n,m,x = list(map(int,input().split()))
l = [0]*n
a = list(map(int,input().split()))
for i in a:
    l[i-1] = 1

left = sum(l[:x])
right = sum(l[x-1:len(l)])

print((left if left<=right else right))

