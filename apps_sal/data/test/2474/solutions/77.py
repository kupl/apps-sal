ans = 0
P = 10**9+7
n = int(input())
c = list(map(int, input().split()))
c = sorted(c)

for i in range(n):
    alr = pow(4, i, P)
    use_bit = n - 1 - i
    flip = pow(2, use_bit, P)
    ret = 1
    if use_bit > 0:
        ret = (pow(2, use_bit, P) + use_bit*pow(2, use_bit-1, P))%P
    ans = (ans + alr*flip*ret*c[i])%P

print(((ans*2)%P))

