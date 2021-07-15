n = int(input())
a = [int(item) for item in input().split()]

a.sort()


s = sum(a)
ans = s

for i in range(len(a)):
    for x in range(2, int(a[i] ** .5) + 1):
        if a[i] % x == 0:
            ans = min(ans, s - a[0] - a[i] + a[0] * x + a[i] // x)

print(ans)

