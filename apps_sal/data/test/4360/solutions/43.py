N = int(input())
Alst = list(map(int, input().split()))
ans = 0
for i in Alst:
    ans += 1/i

print(1/ans)
