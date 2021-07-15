n = int(input())
a = [int(s) for s in input().split()]

a.sort()
b = 10**9 + 1
sum = 0
for i in range(n-1, -1, -1):
    if min(a[i], b - 1) < 1:
        break
    sum += min(a[i], b - 1)
    b = min(a[i], b - 1)

print(sum)

