a, b = list(map(int, input().split(' ')))
x=list(map(int, input().split(' ')))
ptr = 0

while b > 0 and ptr < a:
    if x[ptr]<0:
        x[ptr] = -x[ptr]
        ptr+=1
        b-=1
    else:break

x.sort()
if b > 0:
    b = b % 2
    if b ==1:
        x[0]=-x[0]
print(sum(x))

