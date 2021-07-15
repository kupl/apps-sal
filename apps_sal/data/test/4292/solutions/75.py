n, k = list(map(int, input().split()))
l = list(map(int, input().split()))
l.sort()
result = 0
for data in range(k):
    result += l[data]
print(result)

