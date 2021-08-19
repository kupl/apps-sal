(n, m) = list(map(int, input().split()))
max_pows = -1
temp = n
list_pow = {}
while temp > 0:
    factor = -1
    index = 1
    while index <= temp:
        index *= 2
        factor += 1
    temp = temp - index // 2
    if max_pows == -1:
        max_pows = factor
    list_pow[factor] = 1
min_pows = factor
if len(list_pow) > m:
    print('No')
else:
    pow_count = len(list_pow)
    cur_pow = max_pows
    while pow_count + list_pow[cur_pow] <= m:
        list_pow[cur_pow] -= 1
        if cur_pow - 1 in list_pow:
            list_pow[cur_pow - 1] += 2
        else:
            list_pow[cur_pow - 1] = 2
        pow_count += 1
        if list_pow[cur_pow] == 0:
            cur_pow -= 1
        min_pows = min(min_pows, cur_pow)
    cur_pow = min_pows
    while pow_count != m:
        list_pow[cur_pow] -= 1
        if cur_pow - 1 in list_pow:
            list_pow[cur_pow - 1] += 2
        else:
            list_pow[cur_pow - 1] = 2
        pow_count += 1
        cur_pow -= 1
    print('Yes')
    cur_count = 0
    while cur_count != m:
        if max_pows in list_pow:
            for i in range(list_pow[max_pows]):
                cur_count += 1
                print(max_pows, end=' ')
        max_pows -= 1
