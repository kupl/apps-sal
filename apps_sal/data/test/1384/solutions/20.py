n = int(input())
val = list(map(int, input().split()))
k = 0
for i in range(n + 1):
    k = max(k, i - sum(val[:i]) + sum(val[i:]))
print(k)
