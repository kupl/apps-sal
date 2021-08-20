(n, k) = map(int, input().split())
a = list(map(int, input().split()))
b = []
L = len(bin(k)) - 2
for x in a:
    b.append(bin(x)[2:])
    L = max(L, len(bin(x)) - 2)
for i in range(n):
    b[i] = '0' * (L - len(b[i])) + b[i]
X = 0
for i in range(L):
    if 2 ** (L - i - 1) <= k:
        one = 0
        for j in range(n):
            if b[j][i] == '1':
                one += 1
        if one < n - one:
            k -= 2 ** (L - i - 1)
            X += 2 ** (L - i - 1)
ans = 0
for x in a:
    ans += X ^ x
print(ans)
