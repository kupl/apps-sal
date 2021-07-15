n = int(input())
t_lst = list(map(int, input().split()))
m = int(input())
px_lst = [list(map(int, input().split())) for _ in range(m)]

time_lst = []
for i in range(m):
    problem = px_lst[i][0] - 1
    time = px_lst[i][1]
    before = t_lst[problem]
    t_lst[problem] = time
    time_lst.append(sum(t_lst))
    t_lst[problem] = before

for i in range(m):
    print(time_lst[i])
