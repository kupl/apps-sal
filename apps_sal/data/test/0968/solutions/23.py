def greater(a,b):
    n = [b,a]
    m = sorted(n)
    if n[0] == m[0] :
        return True
    else :
        return False

n = int(input())
name = []
for i in range(n) :
    name.append(sorted(list(input().split())))
p = list(map(int,input().split()))
r = 'YES'
result = [name[p[0]-1][0]]
for i in range(1,n) :
    j = p[i] - 1
    if greater(name[j][0],result[i-1]) :
        result.append(name[j][0])
    elif greater(name[j][1], result[i-1]) :
        result.append(name[j][1])
    else :
        r = 'NO'
        break
print(r)
