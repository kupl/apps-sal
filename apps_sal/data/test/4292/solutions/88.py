N, K = list(map(int, input().split()))
p = list(map(int, input().split()))

p.sort()

sum_p = 0
for i in range(K):
    sum_p += p[i]

print(sum_p)
