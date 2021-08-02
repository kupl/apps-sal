n = int(input())
k = int(input())
x = list(map(int, input().split()))

tot_dis = 0
for i in range(n):
    min_dis = min(x[i], k - x[i])
    tot_dis += 2 * min_dis
print(tot_dis)
