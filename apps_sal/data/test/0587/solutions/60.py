from heapq import heappush,heappop
n,k = map(int,input().split())
kind_value = [[] for _ in range((n+1))]
for i in range(n):
    t,d = map(int,input().split())
    kind_value[t].append(d)
for li in kind_value:
    li.sort()
first_type = [(li[-1],i)for i,li in enumerate(kind_value) if li]
first_type.sort(reverse = True)
kind = 0
value_type1 = 0
second_type = []
second_type_sum = 0
second_type_cnt = 0

answer = 0
for v,i in first_type:
    kind += 1
    if kind > k:
        break
    value_type1 += v
    for d in kind_value[i][:-1]:
        heappush(second_type,d)
        second_type_sum += d
        second_type_cnt += 1
    while second_type_cnt > k-kind:
        d = heappop(second_type)
        second_type_cnt -= 1
        second_type_sum -= d
    value = kind*kind + value_type1 + second_type_sum
    if answer < value:
        answer = value

print(answer)
