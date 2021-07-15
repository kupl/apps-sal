n,m,c = map(int, input().split())
bl = list(map(int, input().split()))

res = 0

for i in range(n):
    al = list(map(int, input().split()))
    temp = c
    for j in range(m):
        temp += al[j]*bl[j]
    if temp >0:
        res +=1
        
print(res)
