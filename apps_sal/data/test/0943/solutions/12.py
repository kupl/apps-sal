n = int(input())

a = [int(s) for s in input().split()]

a.sort()
sum = 0
for i in range(n):
    sum += a[i]
ans = sum
i = 0
while ans % 2 == 1:
    ans = sum - a[i]
    i += 1

print(ans)
