H, W, A, B = list(map(int, input().split()))
C = H - A
D = W - B
p = 1000000007


def power(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return power(a, b // 2) ** 2 % p
    else:
        return power(a, b // 2) ** 2 * a % p


f = [1]
for i in range(H + W):
    f.append(f[i] * (i + 1) % p)

I_f = [0] * (H + W + 1)
I_f[H + W] = power(f[H + W], p - 2)
for i in reversed(list(range(H + W))):
    I_f[i] = I_f[i + 1] * (i + 1) % p


def combi(a, b):
    return f[a + b] * I_f[a] * I_f[b] % p


x = 0
for i in range(C):
    x = (x + combi(i, B - 1) * combi(D - 1, H - i - 1)) % p
print(x)
