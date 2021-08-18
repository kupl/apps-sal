[n, m] = input().split()
n = int(n)
m = int(m)

sum_n = 0
sum_m = 0

for i in range(n):
    sum_n += i

for j in range(m):
    sum_m += j

print(sum_n + sum_m)
