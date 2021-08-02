n = int(input())
a = list(map(int, input().split()))
sum = 0
for i in range(0, n):
    ans = 1 / a[i]
    sum += ans

print(float(1 / sum))
