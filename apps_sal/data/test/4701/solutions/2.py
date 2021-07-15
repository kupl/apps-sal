n = int(input())
k = int(input())

cnt = 1
for _ in range(n):
    cnt = min(cnt*2, cnt+k)
print(cnt)
