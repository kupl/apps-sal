n = int(input())
a = list(map(int, input().split()))
res = 0
for i in range(n):
    res += 1 / a[i]
print(1 / res)
