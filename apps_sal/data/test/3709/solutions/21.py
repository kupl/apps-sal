v = [0 for i in range(20)]
n, m = list(map(int, input().split()))
for i in range(n):
    x = list(map(int, input().split()))
    sum = 0
    for j in range(m):
        sum += x[j] * (1 << j)
    v[sum] = 1
flag = 0
for i in range(16):
    for j in range(16):
        if i & j == 0 and v[i] and v[j]:
            flag = 1

if flag:
    print("YES")
else:
    print("NO")
