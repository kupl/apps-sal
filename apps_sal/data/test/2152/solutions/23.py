n = int(input())
ans = 0
money = float('inf')
for i in range(n):
    (a, b) = map(int, input().split())
    money = min(money, b)
    ans += money * a
print(ans)
