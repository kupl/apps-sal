li = [0] * (10**5 + 10)
n, k = map(int, input().split())
for i in range(n):
    a, b = map(int, input().split())
    li[a] += b
cnt = 0
ans = 0
for i in range(10**5 + 10):
    cnt += li[i]
    ans = i
    if cnt >= k:
        break
print(ans)
