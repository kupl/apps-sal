n = int(input())
p = list(map(int, input().split()))
min = p[0]
count = 1
for i in range(1, n):
    if p[i] <= min:
        count += 1
        min = p[i]
print(count)
