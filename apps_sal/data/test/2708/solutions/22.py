l = list(map(int, input().strip().split()))
n = l[0]
k = l[1]
i = 0
while i < k:
    if n % 10 == 0:
        n = n // 10
    else:
        n -= 1
    i += 1
print(n)
