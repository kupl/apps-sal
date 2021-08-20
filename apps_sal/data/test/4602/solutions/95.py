n = int(input())
k = int(input())
l = list(map(int, input().split()))
ans = 0
for i in l:
    if i >= k / 2:
        ans += abs(k - i) * 2
    else:
        ans += i * 2
print(ans)
