import collections

n = int(input())
vs = list(map(int, input().split()))

vs_even = vs[0::2]
vs_odd = vs[1::2]

count_e = collections.Counter(vs_even).most_common()
count_o = collections.Counter(vs_odd).most_common()

#ダミー
count_e.append((0,0))
count_o.append((0,0))


e_max = len(vs_even) - count_e[0][1]
e_second = len(vs_even) - count_e[1][1]
o_max = len(vs_odd) - count_o[0][1]
o_second = len(vs_odd) - count_o[1][1]

if(count_e[0][0] != count_o[0][0]):
    print(e_max + o_max)

else:
    print(min(e_second+o_max, e_max+o_second))
