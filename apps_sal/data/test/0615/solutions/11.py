import itertools

n = int(input())
lst = list(map(int, input().split()))

lst_accum = list(itertools.accumulate(lst))

min_diff = 10**100
first_cut = 0
third_cut = 2
all_sum = lst_accum[-1]
for k in range(1, len(lst_accum) - 2):
    second_last = lst_accum[k]
    P = lst_accum[first_cut]
    Q = second_last - P
    diff = abs(P - Q)
    while k - first_cut > 1 and diff > abs(second_last - lst_accum[first_cut + 1] * 2):
        first_cut += 1
        P = lst_accum[first_cut]
        Q = second_last - P
        diff = abs(P - Q)

    if third_cut == k:
        third_cut += 1
    third_last = lst_accum[third_cut]
    S = all_sum - third_last
    R = third_last - second_last
    diff = abs(S - R)
    while (n - 1) - third_cut > 1 and diff > abs(all_sum - lst_accum[third_cut + 1] * 2 + second_last):
        third_cut += 1
        third_last = lst_accum[third_cut]
        S = all_sum - third_last
        R = third_last - second_last
        diff = abs(S - R)

    #print(first_cut, k, third_cut)
    min_diff = min(min_diff, max(P, Q, R, S) - min(P, Q, R, S))
    # print(min_diff)


print(min_diff)
