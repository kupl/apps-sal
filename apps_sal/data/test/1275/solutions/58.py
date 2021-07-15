N,K=[int(x) for x in input().split()]

def conb(x):
    if x > N:
        return max((2*N)-x+1,0)
    else:
        return max(x-1,0)

ans = 0

for i in range(1,2*N+1):
    ans += conb(i+K)*conb(i)

print(ans)



