from itertools import product
NS = input()
N = int(NS)


def iter_p_adic(n):
    from itertools import product
    tmp = [('3', '5', '7')] * n
    return product(*tmp)


ans = 0
for k in range(3, len(NS) + 1):
    for i in iter_p_adic(k):
        ls = list(i)
        if ls.count('3') > 0 and ls.count('5') > 0 and ls.count('7') > 0 and int(''.join(ls)) <= N:
            ans += 1
print(ans)
