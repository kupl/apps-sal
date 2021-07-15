s, e, t_per_v = list(map(int, input().split()))
e -= t_per_v
n = int(input())
if n > 0:
    visitors = list(map(int, input().split()))
else:
    visitors=[]

min_wait_time = float("inf")
min_arrive_time = -1
visitor_index = 0
t = s
while t <= e:
    # print(t, visitor_index)
    if visitor_index >= len(visitors) or visitors[visitor_index] > t:
        print(t)
        return
    wait_time = t - visitors[visitor_index]
    if wait_time < min_wait_time:
        min_wait_time = wait_time
        min_arrive_time = visitors[visitor_index]
    t += t_per_v
    visitor_index += 1
print(min_arrive_time - 1)

