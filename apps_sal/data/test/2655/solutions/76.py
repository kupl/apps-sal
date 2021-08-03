n = int(input())
li_a = list(map(int, input().split()))
li_a.sort(reverse=True)
ans = 0
for i in range(1, n):
    ans += li_a[i // 2]
print(ans)
