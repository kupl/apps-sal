n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in a:
    ans += abs(i)

print(ans)

