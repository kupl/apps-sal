n = int(input())
m = int(input())
max_k = 0
sum = 0
min_k = 0
for i in range(n):
    a = int(input())
    sum += a
    min_k = max(min_k, a)

# avg_k = sum / n + (1 if sum % n != 0 else 0)
max_sum = min_k * n
max_k = min_k + m
if max_sum < sum + m:
    m -= (max_sum - sum)
    min_k += m // n + (1 if m % n != 0 else 0)

print(min_k, max_k)
