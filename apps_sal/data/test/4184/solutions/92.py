n = int(input())
w = list(map(int, input().split()))

t = 0
s = sum(w)
ans = sum(w)
for i in range(n):
    t += w[i]
    s -= w[i]
    if abs(s - t) < ans:
        ans = abs(s - t)
print(ans)
