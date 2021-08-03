n = int(input())
a = list(map(int, input().split()))
mx = 0
for i in range(n):
    for j in range(i + 1, n + 1):
        t = sum(a[0:i]) + a[i:j].count(0) + sum(a[j:n])
        if t > mx:
            mx = t

print(mx)
