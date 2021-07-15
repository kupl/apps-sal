n = int(input())
cnt = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    if b - a >= 2:
        cnt += 1
print(cnt)

