n = int(input())
d, x = map(int, input().split())
L = list(int(input()) for _ in range(n))
cnt = x + n

for i in range(n):
    tmp = (d - 1) // L[i]
    cnt += tmp
print(cnt)
