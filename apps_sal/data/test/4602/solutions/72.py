n = int(input())
k = int(input())
x = list(map(int, input().split()))
count = 0
for i in range(n):
    count += min(x[i], k - x[i])
print(count * 2)
