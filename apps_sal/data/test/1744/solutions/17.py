n, m = map(int, input().split())
tot_sum, curr_sum, d = 0, 0, {}
arr = list(map(int, input().split()))
for x in arr:
    tot_sum += x
    curr_sum += x
    curr_res = 0
    for it in sorted(d.keys(), reverse=True):
        if curr_sum <= m:
            break
        take = min(d[it], (curr_sum - m + it - 1) // it)
        curr_sum -= take * it
        curr_res += take
    d[x] = 1 if x not in d else d[x] + 1
    curr_sum = tot_sum
    print(curr_res, end=' ')

