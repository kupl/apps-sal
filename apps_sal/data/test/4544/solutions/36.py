import collections

n = int(input())
a_list = list(map(int, input().split()))
max_cnt = 0

c = collections.Counter(a_list)

for i in range(max(c.keys()) + 1) :
    cnt = c[i] + c[i + 1] + c[i + 2]
    
    if max_cnt < cnt :
        max_cnt = cnt

print(max_cnt)
