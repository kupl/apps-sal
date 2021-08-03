n, h = (int(i) for i in input().split())
ans = 0
l = list(map(int, input().split()))
for i in range(n):
    if l[i] > h:
        ans += 2
    else:
        ans += 1
print(ans)
