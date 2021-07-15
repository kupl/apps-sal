n, t = map(int, input().split())
t_lst = list(map(int, input().split()))
accumulate = 0

for i in range(n - 1):
    time = t_lst[i + 1] - t_lst[i]
    accumulate += min(time, t)

accumulate += t
print(accumulate)
