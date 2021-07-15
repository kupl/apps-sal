n, k = map(int, input().split())
l =  [*map(int, input().split())]
c = 0
res = 0

for i,val in enumerate(l):
    if (val + c) < k and c > 0:
        res += int((val+c)>0)
        c = 0
    else:
        res += (val+c)//k
        c = (val+c)%k
if c > 0: res += 1
print(res)
