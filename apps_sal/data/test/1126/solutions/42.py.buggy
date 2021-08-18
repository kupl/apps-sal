n, x, m = list(map(int, input().split()))
mn = min(n, m)
P = []  # pre_sum
sum_p = 0  # sum of pre + cycle
X = [-1] * m  # for cycle check & pre_len
for i in range(mn):
    if X[x] > -1:
        cyc_len = len(P) - X[x]
        n -= X[x]
        cyc = (sum_p - P[X[x]]) * (n // cyc_len)
        remain = P[X[x] + n % cyc_len]
        print((cyc + remain))
        return
    P.append(sum_p)
    sum_p += x
    X[x] = i
    x = x * x % m
print(sum_p)
