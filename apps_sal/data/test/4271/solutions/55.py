n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

cnt = 0

for i in range(n):
    d = a[i] - 1
    cnt += b[d]

for j in range(n - 1):
    if a[j] + 1 == a[j + 1]:
        cnt += c[a[j] - 1]

print(cnt)
