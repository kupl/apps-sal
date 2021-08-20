N = int(input())
P = tuple(map(int, input().split()))
count = 0
min_num = float('inf')
for i in P:
    if i < min_num:
        count += 1
        min_num = i
print(count)
