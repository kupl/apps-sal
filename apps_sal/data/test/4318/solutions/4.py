n = int(input())
h = list(map(int, input().split()))
a = h[0]
ans = 0
for i in h:
    if i >= a:
        ans += 1
        a = i
print(ans)
