n = int(input())
a = [int(i) for i in input().split()]
sort_a = sorted(a, reverse=True)
now_list = []
next_insert = []
comfort = []
for (index, i) in enumerate(sort_a):
    if len(now_list) == 0:
        now_list += [i]
        next_insert += [1]
        comfort += [i]
    elif len(next_insert) >= n:
        break
    else:
        next_insert += [1, 1]
        comfort += [i, i]
print(sum(comfort[:n - 1]))
