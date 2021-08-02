n = int(input())
k = int(input())
a = [int(x) for x in input().split()]

res = 0

for i in range(n):
    res += min(2 * (abs(a[i])), 2 * (abs(a[i] - k)))

print(res)
