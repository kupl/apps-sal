n, m = map(int, input().split())
al = list(map(int, input().split()))

if n >= m:
    print(0)
    return

al_s = sorted(al)
res=[]
for i in range(m-1):
    res.append(al_s[i+1]-al_s[i])

res_s = sorted(res)

print(sum(res)-sum(res_s[m-n:]))
