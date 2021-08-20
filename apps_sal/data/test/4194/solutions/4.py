(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
sum = 0
for i in a:
    sum += i
if sum > n:
    print(-1)
else:
    print(n - sum)
