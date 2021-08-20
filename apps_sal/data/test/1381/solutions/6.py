from math import ceil
(k, n, s, p) = list(map(int, input().split()))
p_per_person = ceil(n / s)
n_s = k * p_per_person
ans = ceil(n_s / p)
print(ans)
