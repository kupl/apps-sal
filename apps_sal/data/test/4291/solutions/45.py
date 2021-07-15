import sys

input = sys.stdin.readline

n, q= map(int, input().split())

S = input()
S = S.replace('\n','')
s_list = list(S)

l = [0 for i in range(q)]
r = [0 for i in range(q)]
for i in range(q):
    l[i], r[i] = map(int, input().split())

ac_sum_list = [0 for i in range(len(s_list))]
tmp = ""
ac_sum = 0
for i,s in enumerate(s_list):
    if tmp + s == "AC":
        ac_sum += 1
    ac_sum_list[i] = ac_sum
    tmp = s


for i in range(q):
    l_index = l[i]
    r_index = r[i]
    l_ac = ac_sum_list[l_index-1]
    r_ac = ac_sum_list[r_index-1]
    print(r_ac - l_ac)
