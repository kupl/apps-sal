k = int(input())
n = list(map(int, input().split()))

for i in range(k):
    n[i] = bin(n[i])
    n[i] = n[i][2:]

magic = 1000000007


def par(s):
    if s[-1] == '0':
        return True
    else:
        return False


def mod_pow(x, s, p):
    ans = 1
    for i in range(len(s)):
        if s[i] == '1':
            ans = (((ans * ans) % p) * x) % p
        else:
            ans = (ans * ans) % p
    return ans


def div_in_field(a, b, p):
    b_op = pow(b, p - 2, p)
    return (b_op * a) % p


denominator = 2
n_par = False
for i in range(len(n)):
    denominator = mod_pow(denominator, n[i], magic)
    if par(n[i]):
        n_par = True

denominator = div_in_field(denominator, 2, magic)
numerator = 0
if n_par:
    numerator = div_in_field(1 + denominator, 3, magic)
else:
    numerator = div_in_field(-1 + denominator, 3, magic)
ans = str(numerator) + '/' + str(denominator)
print(ans)
