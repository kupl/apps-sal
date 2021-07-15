n = int(input())
b = list(map(int, input().split()))
cur = 0
ans = 0
for i in range(len(b)):
    ans += abs(cur - b[i])
    cur = b[i]
print(ans)
