n,k = map(int, input().split())
al = list(map(int, input().split()))

res= 10**10

for i in range(n-k+1):
    st = al[i]
    en = al[i+k-1]
    if st *en <0:
        temp = min(abs(st),abs(en))*2+max(abs(st),abs(en))
    else:
        temp = max(abs(st),abs(en))
    res = min(temp,res)

print(res)
