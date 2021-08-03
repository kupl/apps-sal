k, n = list(map(int, input().split()))
x = list(map(int, input().split()))
x.sort()
sum = 0
for i in range(n):
    p = x[i]
    sum += p
print(sum)
