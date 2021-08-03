n = int(input())
p = list(map(int, input().split()))
mini = p[0]
ans = 0
for i in p:
    if i <= mini:
        ans += 1
    mini = min(mini, i)
print(ans)
