n = int(input())
a = [0 for i in range(n)]
b = [0 for i in range(n)]
for i in range(n):
    a[i],b[i] = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(n):
        if a[i] == b[j]: cnt += 1
print(cnt)


