(n, m) = map(int, input().split())
l = list(map(int, input().split()))
sum = 0
for i in range(m):
    sum += l[i]
if sum > n:
    print(-1)
else:
    print(n - sum)
