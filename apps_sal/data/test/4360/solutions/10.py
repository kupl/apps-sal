n = int(input())
a = list(map(float, input().split()))
ans = 0
for i in a:
    ans += 1 / i
print(1 / ans)
