n = int(input())
x = list(map(int, input().split()))
p = round(sum(x) / n)
ans = 0
for i in x:
    ans += (i - p)**2
print(ans)
