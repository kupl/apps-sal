# 37
n, k, q = map(int, input().split())
start_point = k - q
list = [start_point for i in range(n)]
for i in range(q):
    list[int(input()) - 1] += 1

for i in range(n):
    if list[i] >= 1:
        print('Yes')
    else:
        print('No')
