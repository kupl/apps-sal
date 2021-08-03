n = int(input())
a = list(map(int, input().split()))
a.sort()
sum = 0
for i in range(0, len(a), 2):
    sum += a[i]
print(sum)
