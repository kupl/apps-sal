n = int(input())
ans = 0
for i in range(n):
    (s, d) = list(map(int, input().split()))
    if ans == 0:
        ans = s
    elif s > ans:
        ans = s
    else:
        ans = d * ((ans - s) // d + 1) + s
print(ans)
