n, l = map(int, input().split())
ans = l
k = 0
sum = 0
for i in range(1, n):
    if abs(ans) > abs(l + i):
        ans = l + i
        k = i
for i in range(n):
    if i != k:
        sum += l + i
print(sum)
