N = int(input())
A = list(map(int, input().split()))
dict1 = {}
for i in range(1, N + 1):
    tmp = i + A[i - 1]
    if tmp not in dict1:
        dict1[tmp] = 1
    else:
        dict1[tmp] += 1
dict2 = {}
for i in range(1, N + 1):
    tmp = i - A[i - 1]
    if tmp not in dict2:
        dict2[tmp] = 1
    else:
        dict2[tmp] += 1
ans = 0
for (k, v) in list(dict1.items()):
    if k in dict2:
        ans += v * dict2[k]
print(ans)
