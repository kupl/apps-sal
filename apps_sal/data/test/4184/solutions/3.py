n = int(input())
a = [int(num) for num in input().split()]
min_i = 100000
for i in range(n):
    if abs(sum(a[0:i + 1]) - sum(a[i + 1:n])) < min_i:
        min_i = abs(sum(a[0:i + 1]) - sum(a[i + 1:n]))
print(min_i)
