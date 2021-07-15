n = int(input())
x = list(map(int, input().split()))
x.sort()
res = 0
for s,i in enumerate(x, 2):
    res += min(n, s) * i
print(res)

