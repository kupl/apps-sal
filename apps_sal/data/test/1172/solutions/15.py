s = input()
n = len(s)
p = 10 ** 9 + 7
q = s.count('?')
l_a = [0] * n
l_x = [0] * n
r_c = [0] * n
r_x = [0] * n
for i in range(1, n):
    l_a[i] = l_a[i - 1] + int(s[i - 1] == 'A')
    l_x[i] = l_x[i - 1] + int(s[i - 1] == '?')
    r_c[n - i - 1] = r_c[n - i] + int(s[n - i] == 'C')
    r_x[n - i - 1] = r_x[n - i] + int(s[n - i] == '?')
ans = 0
pow_q = []
for i in range(0, 4):
    pow_q.append(max(1, 3 ** (q - i) % p))
for i in range(n):
    if s[i] == 'B':
        ans += l_a[i] * r_c[i] % p * pow_q[0] % p
        ans += l_x[i] * r_c[i] % p * pow_q[1] % p
        ans += l_a[i] * r_x[i] % p * pow_q[1] % p
        ans += l_x[i] * r_x[i] % p * pow_q[2] % p
        ans %= p
    elif s[i] == '?':
        ans += l_a[i] * r_c[i] % p * pow_q[1] % p
        ans += l_x[i] * r_c[i] % p * pow_q[2] % p
        ans += l_a[i] * r_x[i] % p * pow_q[2] % p
        ans += l_x[i] * r_x[i] % p * pow_q[3] % p
        ans %= p
print(ans)
