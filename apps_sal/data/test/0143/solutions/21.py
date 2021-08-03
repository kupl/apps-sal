n = int(input())
a = list(map(int, input().split()))
a.sort()

target = 1
for i in range(n):
    if a[i] >= target:
        target += 1

print(target)
