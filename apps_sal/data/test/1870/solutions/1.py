n, c = (int(i) for i in input().split())
l = list(map(int, input().split()))
ans = 1
for i in range(1, n):
    if l[i] - l[i - 1] > c:
        ans = 1
    else:
        ans += 1
print(ans)
