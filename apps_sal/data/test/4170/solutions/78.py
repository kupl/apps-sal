n = int(input())
h = list(map(int, input().split()))
result = 0
tmp = 0
for i in range(n - 1):
    if h[i] >= h[i + 1]:
        tmp += 1
        result = max(result, tmp)
    else:
        tmp = 0
print(result)
