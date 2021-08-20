n = int(input())
a = list(map(int, input().split()))
seisu = [0] * n
sum = 0
for i in range(n):
    seisu[a[i] - 1] += 1
for i in range(n):
    sum += seisu[i] * (seisu[i] - 1) // 2
for i in range(n):
    if seisu[a[i] - 1] >= 2:
        ans = sum - seisu[a[i] - 1] * (seisu[a[i] - 1] - 1) // 2 + (seisu[a[i] - 1] - 1) * (seisu[a[i] - 1] - 2) // 2
    else:
        ans = sum
    print(ans)
