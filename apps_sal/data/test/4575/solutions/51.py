n = int(input())
(d, x) = map(int, input().split())
a = [int(input()) for i in range(n)]
cnt = x
for i in range(n):
    for j in range(d):
        if a[i] * j + 1 <= d:
            cnt += 1
print(cnt)
