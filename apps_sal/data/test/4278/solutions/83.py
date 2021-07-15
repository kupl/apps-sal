from collections import Counter

N = int(input())
s_list = []
for i in range(N):
    s = input()
    s_min = sorted(s)
    s_min_join = "".join(s_min)
    s_list.append(s_min_join)

s_list_c = Counter(s_list)

ans = 0
for j in list(s_list_c.values()):
    ans += j*(j-1)//2

print(ans) 
