n = int(input())
a = list(map(int, input().split()))
i = 1
m = -1
ans = -1
for x in a:
    if x > m + 1:
        ans = i
        break
    else:
        i = i + 1
        m = max(m, x)
print(ans)
