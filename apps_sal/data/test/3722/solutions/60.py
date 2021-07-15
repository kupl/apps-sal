n = int(input())
t = {"A":0, "B":1}

aa = t[input()]
ab = t[input()]
ba = t[input()]
bb = t[input()]

max_n=n+10
mod=10**9+7

frac=[1]
for i in range(1,max_n+1):
    frac.append((frac[-1]*i)%mod)

inv=[1,1]
inv_frac=[1,1]
for i in range(2,max_n):
    inv.append((mod-inv[mod%i]*(mod//i))%mod)
    inv_frac.append((inv_frac[-1]*inv[-1])%mod)

def perm(m,n):
    if m<n:
        return 0
    if m==1:
        return 1
    return (frac[m]*inv_frac[m-n])%mod

def comb(m,n):
    if m<n:
        return 0
    if m==1:
        return 1
    return (frac[m]*inv_frac[n]*inv_frac[m-n])%mod

if ab == 1:
    ab = 1 - ab
    ba = 1 - ba
    aa,bb = 1 - bb, 1 - aa


if aa == 0:
    print((1))
elif ba == 1:
    if n <= 3:
        print((1))
    else:
        print((pow(2, n-3, mod)))
else:
    c = 0
    for i in range(1,n//2+1):
        c = (c + comb(n-i-1, i-1)) % mod
    print(c)

