N = int(input())
S1 = input()
S2 = input()
mod = 10**9+7

ans = 1
if(S1[0] == S2[0]):
    ans *= 3
    ans %= mod
    
    idx = 1
else:
    ans *= 6
    ans %= mod
    idx = 2

while(idx <= N-1):
    if(S1[idx] == S2[idx]):
        if(S1[idx-1] == S2[idx-1]):
            ans *= 2
            ans %= mod
            idx += 1
        else:
            ans *= 1
            ans %= mod
            idx += 1
    else:
        if(S1[idx-1] == S2[idx-1]):
            ans *= 2
            ans %= mod
            idx += 2
        else:
            ans *= 3
            ans %= mod
            idx += 2
print(ans)
