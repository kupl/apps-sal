import sys
# with open(filename, 'r') as f:
with sys.stdin as f:
    n, C = f.readline().split(" ")
    n, C = int(n), int(C)
p = 1000003


def compute_mod_fact(n, p):
    # n! (mod p)
    res = 1
    for i in range(1, n + 1):
        res = (res * i) % p
    return res


def compute_mod_mult(n, a, p):
    # n**a (mod p)
    res = 1
    for _ in range(a):
        res = (res * n) % p
    return res


res = compute_mod_fact(n + C, p)
res1 = compute_mod_fact(n, p)
res1 = compute_mod_mult(res1, p - 2, p)
res2 = compute_mod_fact(C, p)
res2 = compute_mod_mult(res2, p - 2, p)
#print(res, res1, res2)
res = (res * res1 * res2 - 1) % p
print(res)
