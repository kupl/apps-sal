(n, k) = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
sum = 0
for i in range(k):
    sum = sum + a[i]
print(sum)
