N = int(input())
A = list(map(int, input().split()))
M = []
for i in A:
    if i % 2 == 0:
        M.append(i)
ans = 0
for j in M:
    while j % 2 == 0:
        j //= 2
        ans += 1
print(ans)
