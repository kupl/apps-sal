n = int(input())
(d, x) = list(map(int, input().split()))
ans = x
for i in range(n):
    a = int(input())
    if d - 1 > 0:
        ans += int((d - 1) / a) + 1
    else:
        ans += 1
print(ans)
