import heapq
n, m = list(map(int, input().split()))
job_list = []
for i in range(n):
    tmp = [int(x) for x in input().split()]
    job_list.append(tmp)
job_list.sort()

k = 0
ans = 0
salary_list = []
for i in range(1, m + 1):
    while k < n and job_list[k][0] == i:
        heapq.heappush(salary_list, job_list[k][1] * (-1))
        k += 1
    if len(salary_list) > 0:
        ans += heapq.heappop(salary_list)
print(((-1) * ans))
