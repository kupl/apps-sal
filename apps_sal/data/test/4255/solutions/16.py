a,b,c = map(int, input().split())

d = max(a,b,c)

res = 1

if a !=d:
    res *=a

if b !=d:
    res *=b

if c !=d:
    res *=c
    
print(res//2)
