(n, k, x) = map(int, input().split())
time = list(map(int, input().split()))
sum = 0
for i in range(n - k):
    sum = time[i] + sum
total = sum + k * x
print(total)
