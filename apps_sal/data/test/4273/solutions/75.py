import itertools
n = int(input())  # nは入力回数
#num_list = [int(input()) for _ in range(n)]
ans = 0

set_m = set()
set_a = set()
set_r = set()
set_c = set()
set_h = set()

for i in range(n):
    s = input()
    if s[0] == "M":
        set_m.add(s)
    if s[0] == "A":
        set_a.add(s)
    if s[0] == "R":
        set_r.add(s)
    if s[0] == "C":
        set_c.add(s)
    if s[0] == "H":
        set_h.add(s)

l_m = len(set_m)
l_a = len(set_a)
l_r = len(set_r)
l_c = len(set_c)
l_h = len(set_h)

l_l = [l_m, l_a, l_r, l_c, l_h]

comb_list = list(itertools.combinations(l_l, 3))

for i in range(len(comb_list)):
    ans += comb_list[i][0] * comb_list[i][1] * comb_list[i][2]

print(ans)
