from collections import Counter

n = int(input())
izms = Counter(list(map(int, input().split())))


max_val = max(izms)
min_val = min(izms)
max_cnt = izms[max_val]
min_cnt = izms[min_val]
med_cnt = n - max_cnt - min_cnt
res = n

# print(' '.join(' '.join([str(iz)]*izms[iz]) for iz in izms), izms)

if max(izms) - min(izms) == 2:
    med_val = max(izms) - 1
    krainie = min(max_cnt, min_cnt)
    if krainie > med_cnt // 2:
        res -= 2 * krainie
        izms[max_val] -= krainie
        izms[min_val] -= krainie
        izms[med_val] += krainie * 2
    else:
        srednie = 2 * (med_cnt // 2)
        res -= srednie
        izms[med_val] -= srednie
        izms[max_val] += (med_cnt // 2)
        izms[min_val] += (med_cnt // 2)


print(res)
a = [' '.join([str(iz)] * izms[iz]) for iz in izms]
print(' '.join(k for k in a if len(k) > 0))
