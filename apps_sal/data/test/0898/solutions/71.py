N,M = map(int,input().split())

# 約数列挙
def enum_div(N):
    ret = []
    for i in range(1,int(N**0.5)+1):
        if N % i == 0:
            ret.append(i)
            if i**2 != N:
                ret.append(N // i)
        i += 1
    return ret

ans = 0
for i in enum_div(M):
    if i >= N:
        ans = max(ans,M // i)

print(int(ans))
