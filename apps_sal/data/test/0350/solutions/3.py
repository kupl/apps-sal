n = [int(s) for s in input().split()]
a = [int(s) for s in input().split()]
x = set()
res = 0
for i in reversed(sorted(a)):
    while i>0:
        if i in x:
            i-=1
        else:
            res+=i
            x.add(i)
            break
print(res)

