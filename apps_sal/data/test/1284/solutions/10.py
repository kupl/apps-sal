N = int(input())
A = list(map(int,input().split()))
cumev = [0]
cumod = [0]
for i,a in enumerate(A):
    cumev.append(cumev[-1] + (a if i%2==0 else 0))
    cumod.append(cumod[-1] + (a if i%2 else 0))

ans = cumev[-1]
for i,(e,o) in enumerate(zip(cumev,cumod)):
    if i%2:
        tmp = e + cumod[-1] - o
    else:
        tmp = o + cumev[-1] - e
    ans = max(ans,tmp)
print(ans)

