n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
res = 1
for i in range(n):
    res *= a[i]
    if res > 10**18:
        res = -1
        break
print(res)
