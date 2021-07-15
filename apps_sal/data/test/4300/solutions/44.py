n = int(input())
d = list(map(int, input().split()))
a = 0
for i in range(n):
    for j in range(n):
        if i != j:
            a += d[i] * d[j]
print(a // 2)
