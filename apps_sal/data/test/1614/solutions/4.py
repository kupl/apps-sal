n, h = list(map(int, input().split()))
ai = list(map(int, input().split()))
ans = 0
for i in range(n):
    if ai[i] > h:
        ans += 2
    else:
        ans += 1
print(ans)
