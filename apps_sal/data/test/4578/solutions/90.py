N, X = map(int, input().split())
donut_list = []
for i in range(N):
    donut_list.append(int(input()))

donut_sum = sum(donut_list)
X_remaining = X - donut_sum
donut_num = N
donut_num += int(X_remaining / min(donut_list))

print(donut_num)
