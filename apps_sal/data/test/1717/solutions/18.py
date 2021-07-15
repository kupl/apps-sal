n = int(input())
j = 2
v = 2
def johou(a,b):
    mx = max(a,b)
    mn = min(a,b)
    while True:
        tmp = mn
        mn = mx % mn
        mx = tmp
        if mn == 0:
            return mx
            break
for i in range(2,n+1):
    j = johou(v,i)
    v = i*v/j
print(int(v+1))
