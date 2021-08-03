N = int(input())
aaa = list(map(int, input().split()))
bbb = [format(a, '061b') for a in aaa]

zero = [0] * 61
one = [0] * 61
for i in range(61):
    s = ''.join(list(b[-(i + 1)] for b in bbb))
    zero[i] = s.count('0')
    one[i] = s.count('1')
ans = 0
MOD = 1_000_000_007
for i, o, l in zip(list(range(61)), zero, one):
    ans += 2**i * o * l
    ans %= MOD
print(ans)
