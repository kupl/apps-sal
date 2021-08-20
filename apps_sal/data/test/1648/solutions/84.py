(N, B) = list(map(int, input().split()))
R = N - B
mod = pow(10, 9) + 7
ans = [0] * (B + 1)
Bn = B - 1
Rn = R + 1
if R + 1 < B:
    Br = B - R - 1
    Bbunshi = 1
    Bbunbo = 1
    for i in range(Br):
        Bbunshi = Bbunshi * (Bn - i) % mod
        Bbunbo = Bbunbo * (i + 1) % mod
    Rbunshi = 1
    Rbunbo = 1
    Rr = 1
    Bn -= Br
    Br += 1
    ans[R + 1] = Bbunshi * pow(Bbunbo, -1, mod) % mod
elif R + 1 > B:
    Rr = R - B + 1
    Rbunshi = 1
    Rbunbo = 1
    for i in range(Rr):
        Rbunshi = Rbunshi * (Rn - i) % mod
        Rbunbo = Rbunbo * (i + 1) % mod
    Bbunshi = 1
    Bbunbo = 1
    Br = 1
    Rn -= Rr
    Rr += 1
    ans[B] = Rbunshi * pow(Rbunbo, -1, mod) % mod
else:
    Br = 1
    Bbunshi = 1
    Bbunbo = 1
    Rr = 1
    Rbunshi = 1
    Rbunbo = 1
    ans[B] = 1
n = min(R + 1, B)
for i in range(n - 1, 0, -1):
    Bbunshi = Bbunshi * Bn % mod
    Bbunbo = Bbunbo * Br % mod
    Rbunshi = Rbunshi * Rn % mod
    Rbunbo = Rbunbo * Rr % mod
    ans[i] = Bbunshi * pow(Bbunbo, -1, mod) * (Rbunshi * pow(Rbunbo, -1, mod)) % mod
    Bn -= 1
    Rn -= 1
    Br += 1
    Rr += 1
for i in range(1, B + 1):
    print(ans[i])
