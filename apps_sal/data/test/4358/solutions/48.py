N = int(input())

p_sum = 0
p_max = 0
for i in range(N):
    p = int(input())
    p_sum += p
    p_max = max(p_max, p)

print(p_sum - p_max // 2)
