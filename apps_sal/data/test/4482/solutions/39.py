
N = int(input())
list = [int(a) for a in input().split()]

A = sum(list)//N
ans = 0

for k in range(N):
    ans = ans + (list[k] - A) ** 2

for i in range(-100,100):
    sum_new = 0
    for j in range(N):
        sum_new = sum_new + (list[j] - i) ** 2
    if(ans > sum_new):
        ans = sum_new

print(ans)

