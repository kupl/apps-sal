N = int(input())
ans = 1
for i in range(1, N):
    if i*i > N:
        break
    ans = max(ans, i*i)
print(ans)
