n = int(input())
x = list(map(int, input().split()))
count = 1
m = x[0]
for i in range(1, n):
    if m >= x[i]:
        count += 1
        m = x[i]
print(count)
