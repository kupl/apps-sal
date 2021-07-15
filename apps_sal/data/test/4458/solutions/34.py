n = int(input())
s = list(map(int, input().split()))

min = s[0]
ans = 0

for i in range(n):
    if min >= s[i]:
        min = s[i]
        ans += 1

print(ans)

