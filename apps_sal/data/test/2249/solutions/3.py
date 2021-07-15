n = int(input())
a = [int(x) for x in input().split()]

MAX_NUM = 100010
met_forw = [False] * MAX_NUM
met_backw = [False] * MAX_NUM
unique_n_backw = [0] * n

for i in range(n - 1, -1, -1):
    if i < n - 1:
        unique_n_backw[i] = unique_n_backw[i + 1]
    if not met_backw[a[i]]:
        met_backw[a[i]] = True
        unique_n_backw[i] += 1

answer = 0
for i in range(n - 1):
    if not met_forw[a[i]]:
        met_forw[a[i]] = True
        answer += unique_n_backw[i + 1]

print(answer)

