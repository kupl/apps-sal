N = int(input())
p = [int(input()) for _ in range(N)]

p_sum = 0
p_max = 0
for i in range(N):
    p_sum += p[i]
    p_max = max(p_max, p[i])

print(p_sum - p_max // 2)
