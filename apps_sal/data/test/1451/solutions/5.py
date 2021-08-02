n, k = list(map(int, input().split()))

A = list(input().split())
ans = 0
for item in A:
    if(item.count('4') + item.count('7') <= k):
        ans += 1
print(ans)
