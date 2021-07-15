n=int(input()) 
c=list(map(int, input().split()))
s = sum(c)
l = []
x = 0
y = s

for i in c[:n-1]:
    x += i
    y -= i
    l += [abs(x-y)]
print(min(l))
