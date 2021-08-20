n = int(input())
h = list(map(int, input().split()))
h.append(10 ** 9 + 1)
c = 0
ans = 0
for i in range(n):
    if h[i] >= h[i + 1]:
        c += 1
        ans = max(ans, c)
    else:
        ans = max(ans, c)
        c = 0
print(ans)
