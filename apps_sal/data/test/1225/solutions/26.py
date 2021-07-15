n = int(input())
cnt = 0
while n != 1:
    n = n // 2
    cnt += 1
ans = 1
for i in range(1, cnt+1):
    ans = ans + (2**i)
print(ans)
