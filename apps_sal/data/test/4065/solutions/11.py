n = int(input())
u = list(map(int, input().split()))
ans = 0
p = 1
for i in range(1, n):
    if u[i - 1] * 2 >= u[i]:
        p += 1
    else:
        if p > ans:
            ans = p
        p = 1
if p > ans:
    ans = p
print(ans)
