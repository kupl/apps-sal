n = int(input())
a = list(map(int, input().split()))
ans = 0
cur = 0
for i in range(n):
    if (a[i] >= 4):
        cur += 1
    else:
        cur = 0
    if (cur == 3):
        ans += 1
        cur = 0
print(ans)
