import collections

n = int(input())
v = list(map(int, input().split()))
even_odd_length = n / 2
replace_total = 0

list_odd = v[0::2]
list_even = v[1::2]

dict_c_odd = dict(collections.Counter(list_odd))
dict_c_even = dict(collections.Counter(list_even))
dict_c_even_bk = dict_c_even.copy()
dict_c_odd_bk = dict_c_odd.copy()

replace_total_tmp = 0
replace_total_tmp2 = 0
max_count_c_odd = max(dict_c_odd.values())
max_count_c_even = max(dict_c_even.values())
max_count_c_even_bk = max_count_c_even
max_c_odd_keys = [k for k, v in dict_c_odd.items() if v == max_count_c_odd]
max_c_even_keys = [k for k, v in dict_c_even.items() if v == max_count_c_even]

if len(set(v)) == 1:
    print(int(even_odd_length))
else:    
    if max_c_odd_keys[0] in dict_c_even:
        del dict_c_even[max_c_odd_keys[0]]
    max_count_c_even = max(dict_c_even.values())
    replace_total_tmp = (n - max_count_c_odd - max_count_c_even)
    
    dict_c_even = dict_c_even_bk
    max_count_c_even = max_count_c_even_bk
    
    if max_c_even_keys[0] in dict_c_odd:
        del dict_c_odd[max_c_even_keys[0]]
    max_count_c_odd = max(dict_c_odd.values())
    replace_total_tmp2 = (n - max_count_c_odd - max_count_c_even)
    
    if replace_total_tmp >= replace_total_tmp2:
         replace_total = replace_total_tmp2
    else:
         replace_total = replace_total_tmp
    print(replace_total)
