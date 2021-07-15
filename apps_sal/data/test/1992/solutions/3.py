n,m,k = input().split()
n = int(n)
m = int(m)
k = int(k)
p = [int(x) for x in input().split()]
o = [int(x) for x in input().split()]
g = 0
pos = {}
val = {}
j = 0
for i in p:
    pos[i] = j
    val[j] = i
    j += 1
for i in o:
    ind = pos[i]
    g += ((ind)//k)+1
    if ind > 0:
        tmp = val[ind-1]
        val[ind-1] = i
        pos[i] = ind -1
        val[ind] = tmp
        pos[tmp] = ind

print(g)
