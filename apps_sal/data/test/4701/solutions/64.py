n = int(input())
k = int(input())

res = 1
for i in range(n):
    if res >= k:
        res += k
    else:
        res *= 2
print(res)
