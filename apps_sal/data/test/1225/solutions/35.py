h = int(input())

cnt = 0
while h != 1:
    h //= 2
    cnt += 1
t = 1
ans = 0
for i in range(cnt+1):
    ans += t
    t *= 2
print(ans)
