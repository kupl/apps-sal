n = int(input())
cnt = 0
for i in range(n):
    p, q = map(int, input().split())
    if p <= q - 2:
        cnt += 1
print(cnt)
