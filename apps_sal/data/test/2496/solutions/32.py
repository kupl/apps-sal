max_num = 10**6 + 1
prime = [i for i in range(max_num)]
r2_num = int(max_num**(1 / 2)) + 1
for i in range(2, r2_num):
    if prime[i] == i:
        for j in range(i**2, max_num, i):
            if prime[j] == j:
                prime[j] = i


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


flg_pairwise = True
flg_setwise = False

n = int(input().rstrip())
a_ls = list(map(int, input().rstrip().split(" ")))
gcd_a = 0
primes_a = []
count_prime = [0 for i in range(max_num)]
for a in a_ls:
    gcd_a = gcd(gcd_a, a)
    if gcd_a == 1:
        flg_setwise = True
    tmp_prime = 0
    while a > 1:
        p = prime[a]
        pp = prime[p]
        if p == 0 or pp == 0:
            flg_pairwise = False
            break
        if tmp_prime != p:
            prime[tmp_prime] = 0
            tmp_prime = p
        a = a // p
    if flg_pairwise:
        prime[tmp_prime] = 0
    if flg_setwise and not flg_pairwise:
        break
if flg_pairwise:
    print("pairwise coprime")
elif flg_setwise:
    print("setwise coprime")
else:
    print("not coprime")
