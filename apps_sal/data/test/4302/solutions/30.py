AB = list(map(int, input().split()))
ans = 0
for i in range(2):
    ans += max(AB)
    AB[AB.index(max(AB))] -= 1
print(ans)
