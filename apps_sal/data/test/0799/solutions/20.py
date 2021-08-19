n = int(input())
a = [int(i) for i in input().split()]
m = max(a)
min_sum = 0
for elem in a:
    min_sum += m - elem
print(min_sum)
