import numpy as np

def binstr(n):
    return np.array(list(map(int,list(bin(n)[2:].rjust(40,'0')))))

N,K = map(int,input().split())
A = list(map(int,input().split()))

AA = sum([binstr(i) for i in A])
X = 0
ans = 0
for i in range(40):
    if AA[i] > N-AA[i]:   # 0にした方がいい
        ans += AA[i]*(2**(39-i))
    else:                 # 1にした方がいい
        if X+2**(39-i) <= K:    # 1
            ans += (N-AA[i])*(2**(39-i))
            X += 2**(39-i)
        else:                  # 0
            ans += AA[i]*(2**(39-i))

print(ans)
