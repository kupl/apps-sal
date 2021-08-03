n, d = list(map(int, input().split()))
check = "1" * n
ans = 0
cur = 0
for i in range(d):
    s = input()
    if s != check:
        cur += 1
        ans = max(ans, cur)
    else:
        cur = 0
print(ans)
