from itertools import accumulate


def divisors(n):
    lst = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            lst.append(i)
            if i != n // i: lst.append(n // i)
    return lst


N, K = map(int, input().split())
*A, = map(int, input().split())
cands = divisors(sum(A))
for d in sorted(cands, reverse=True):
    rems = sorted([a % d for a in A])
    cumsum_rems = [0] + list(accumulate(rems))
    for i in range(1, N):
        minus = cumsum_rems[i]
        plus = d * (N - i) - (cumsum_rems[N] - minus)
        if max(minus, plus) <= K: break
    else:
        continue
    break
print(d)
