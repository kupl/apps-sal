n, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
ans = 0
for i in range(0, k):
    ans += lst[i]

print(ans)
