N, X = [int(_) for _ in input().split()]
D = [int(_) for _ in input().split()]

days_per_year = sum(D)
year_value = sum([(d * (d + 1)) // 2 for d in D])


answer = year_value * (X // days_per_year)
X = X % days_per_year


answer_year = 0
i = N
pm = N - 1
pd = D[N - 1]
c = 0
to_add = None
while i >= 0:
    if i < N:
        c -= (D[i] * (D[i] + 1)) // 2
    if to_add is None:
        to_add = X
    else:
        to_add = D[i]
    while D[pm] - (D[pm] - pd) <= to_add:
        to_add -= D[pm] - (D[pm] - pd)
        c += (pd * (pd + 1)) // 2
        pm -= 1
        if pm < 0:
            pm = N - 1
        pd = D[pm]
    h = pd
    pd -= to_add
    l = pd
    c += ((h * (h + 1)) // 2) - ((l * (l + 1)) // 2)
    answer_year = max(answer_year, c)
    i -= 1

answer += answer_year
print(answer)
