n = int(input())
MOD = 998244353

if n == 1:
    print((pow(2, MOD - 2, MOD)))
    return

if n == 2:
    print((1))
    print((1))
    return

div = pow(pow(2, n - 1, MOD), MOD - 2, MOD)
num = n * pow(2, n - 2, MOD) % MOD
a = 1
b = 3
buf = [div * num % MOD] * 2
for i in range((n + 1) // 2 - 2):
    num = (num + a * b) % MOD
    buf.append(div * num % MOD)
    a = a * 4 % MOD
    b = (b + 2) % MOD
if n % 2 == 0:
    buf.extend(list(reversed(buf)))
else:
    buf.extend(list(reversed(buf[:-1])))

print(('\n'.join(map(str, buf))))

