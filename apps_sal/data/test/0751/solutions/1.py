n, m = list(map(int, input().split()))
p = list(map(int, input().split()))

bn = 0
ib = 0

for i in p:
    if ib+i>m:
        ib=i
        bn+=1
    else:
        ib+=i
if ib > 0:
    bn += 1

print(bn)

